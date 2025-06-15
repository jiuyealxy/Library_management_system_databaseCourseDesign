-- 根据外键依赖依次删除已有表
DROP TABLE IF EXISTS borrow;
DROP TABLE IF EXISTS item;
DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS bookshelfs;
DROP TABLE IF EXISTS loginrecord;
DROP TABLE IF EXISTS readers;
DROP TABLE IF EXISTS readertype;
DROP TABLE IF EXISTS workers;

-- 书架信息
CREATE TABLE bookshelfs  (
  书架号 varchar(10) NOT NULL,
  书籍类型 varchar(45) NOT NULL,
  PRIMARY KEY (书架号) USING BTREE
);

INSERT INTO bookshelfs VALUES ('C01', '计算机技术'),('C02', '自动化'),('C03', '文学'),('A01', '人工智能'),('B01', '航空航天'),
                              ('C04', '材料科学'),('A02', '自动化控制'),('B02', '经济管理'),('C05', '外语学习'),
                              ('A03', '文学艺术'),('B03', '马克思主义理论'),('B04', '物理科学'),('A04', '人文社科');

-- 图书信息
CREATE TABLE books  (
  书号 varchar(15) NOT NULL,
  书名 varchar(30) NOT NULL,
  作者 varchar(20) DEFAULT NULL,
  类型 varchar(15) DEFAULT NULL,
  价格 float DEFAULT NULL,
  出版社 varchar(45) DEFAULT NULL,
  摘要 varchar(50) DEFAULT NULL,
  馆藏册数 int(0) DEFAULT NULL,
  在馆册数 int(0) DEFAULT NULL,
  书架号 varchar(15) DEFAULT NULL,
  被借次数 int(0) DEFAULT NULL,
  PRIMARY KEY (书号) USING BTREE,
  INDEX 书架号_idx(书架号) USING BTREE,
  CONSTRAINT 书架号 FOREIGN KEY (书架号) REFERENCES bookshelfs (书架号) ON DELETE RESTRICT ON UPDATE RESTRICT
) ;

-- 读者类型表
CREATE TABLE readertype  (
  读者类型 varchar(10)  NOT NULL,
  借书时间 int(0) DEFAULT NULL,
  最多在借册数 int(0) DEFAULT NULL,
  PRIMARY KEY (读者类型) USING BTREE
);

INSERT INTO readertype VALUES ('教师', 3, 30);
INSERT INTO readertype VALUES ('本科生', 1, 10);
INSERT INTO readertype VALUES ('研究生', 2, 20);

-- 读者表
CREATE TABLE readers  (
  ID varchar(15) NOT NULL,
  姓名 varchar(20) NOT NULL,
  性别 enum('男','女') DEFAULT NULL,
  单位 varchar(45) DEFAULT NULL,
  读者类型 varchar(45) DEFAULT NULL,
  可借册数 int(0) DEFAULT NULL,
  在借册数 int(0) DEFAULT NULL,
  password varchar(20) NOT NULL DEFAULT '123456',
  欠款 float NOT NULL DEFAULT 0,
  PRIMARY KEY (ID) USING BTREE,
  CONSTRAINT 读者类型 FOREIGN KEY (读者类型) REFERENCES readertype (读者类型) ON DELETE RESTRICT ON UPDATE RESTRICT
);

-- 借书记录
CREATE TABLE borrow  (
  ID varchar(15) NOT NULL,
  书号 varchar(15) NOT NULL,
  借书时间 date NOT NULL,
  PRIMARY KEY (ID, 书号, 借书时间) USING BTREE,
  INDEX 书号_idx(书号) USING BTREE,
  CONSTRAINT ID FOREIGN KEY (ID) REFERENCES readers (ID) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT 书号 FOREIGN KEY (书号) REFERENCES books (书号) ON DELETE RESTRICT ON UPDATE RESTRICT
);

-- 借书/还书申请
CREATE TABLE item  (
  bookid varchar(15) NOT NULL,
  ID varchar(15) NOT NULL,
  time date NOT NULL,
  type enum('borrow','return') NOT NULL,
  PRIMARY KEY (bookid, ID, time, type) USING BTREE,
  INDEX readerid_idx(ID) USING BTREE,
  CONSTRAINT bookid FOREIGN KEY (bookid) REFERENCES books (书号) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT readerid FOREIGN KEY (ID) REFERENCES readers (ID) ON DELETE RESTRICT ON UPDATE RESTRICT
);

-- 登陆记录
CREATE TABLE loginrecord  (
  ID varchar(15) NOT NULL,
  time date NOT NULL,
  number int(0) NOT NULL,
  PRIMARY KEY (time, number) USING BTREE,
  INDEX readerid_idx(ID) USING BTREE,
  CONSTRAINT readerid2 FOREIGN KEY (ID) REFERENCES readers (ID) ON DELETE RESTRICT ON UPDATE RESTRICT
);

-- 工作人员
CREATE TABLE workers  (
  ID varchar(15) NOT NULL,
  姓名 varchar(20) NOT NULL,
  type enum('图书管理员','系统管理员') NOT NULL,
  password varchar(20) NOT NULL DEFAULT '123456',
  PRIMARY KEY (ID, type) USING BTREE
);

INSERT INTO workers VALUES ('01', '落兮呀', '系统管理员', '050330zzp');
INSERT INTO workers VALUES ('10001', '张三', '图书管理员', '123456');

-- 读者初始化触发器
DELIMITER //
CREATE TRIGGER set_borrow_limit_on_insert
BEFORE INSERT ON readers
FOR EACH ROW
BEGIN
  SET NEW.可借册数 = (
    SELECT 最多在借册数 FROM readertype WHERE 读者类型 = NEW.读者类型
  );
END;
//
DELIMITER ;

-- 删除读者时的触发器，删除对应登陆记录
DELIMITER //
CREATE TRIGGER delete_reader_login_record
BEFORE DELETE ON readers
FOR EACH ROW
BEGIN
  DELETE FROM loginrecord WHERE ID = OLD.ID;
END;
//
DELIMITER ;

-- 批准借书时的自动操作
DELIMITER //
CREATE TRIGGER after_item_delete_borrow
AFTER DELETE ON item
FOR EACH ROW
BEGIN
  IF OLD.type = 'borrow' THEN
    -- 插入 borrow 表
    INSERT INTO borrow(ID, 书号, 借书时间)
    VALUES (OLD.ID, OLD.bookid, OLD.time);

    -- 更新 readers 表
    UPDATE readers
    SET 可借册数 = 可借册数 - 1,
        在借册数 = 在借册数 + 1
    WHERE ID = OLD.ID;

    -- 更新 books 表
    UPDATE books
    SET 在馆册数 = 在馆册数 - 1,
        被借次数 = 被借次数 + 1
    WHERE 书号 = OLD.bookid;
  END IF;
END;
//
DELIMITER ;

-- 批准还书时的自动操作
DELIMITER //
CREATE TRIGGER after_item_delete_return
AFTER DELETE ON item
FOR EACH ROW
BEGIN
  IF OLD.type = 'return' THEN
    -- 删除 borrow 表中的借阅记录
    DELETE FROM borrow
    WHERE ID = OLD.ID AND 书号 = OLD.bookid;

    -- 更新 readers 表
    UPDATE readers
    SET 可借册数 = 可借册数 + 1,
        在借册数 = 在借册数 - 1
    WHERE ID = OLD.ID;

    -- 更新 books 表
    UPDATE books
    SET 在馆册数 = 在馆册数 + 1
    WHERE 书号 = OLD.bookid;
  END IF;
END;
//
DELIMITER ;

SET FOREIGN_KEY_CHECKS = 1;