-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: localhost    Database: shiyan
-- ------------------------------------------------------
-- Server version	8.0.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `agency`
--

DROP TABLE IF EXISTS `agency`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `agency` (
  `ano` char(8) NOT NULL,
  `aname` char(8) DEFAULT NULL,
  `asex` char(1) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `aphone` char(12) DEFAULT NULL,
  `aremark` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ano`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `agency`
--

LOCK TABLES `agency` WRITE;
/*!40000 ALTER TABLE `agency` DISABLE KEYS */;
INSERT INTO `agency` VALUES ('1','李华','男','18312992151','8'),('11','叶文','男','2144511222','11'),('12','罗澄','男','1452221475','12'),('13','郑隆','男','1457525265','13'),('18','黄兴','男','1921545487','44'),('19','李伟','男','15451213645','12121'),('2','梁建海','男','18312992151','8'),('20','叶璇','男','1548451212','1213'),('3','张蹇','男','1549566416','12312'),('4','张晓静','女','123456789','4'),('5','李云龙','男','1231545','5'),('55','罗篓','男','1524855151','121213'),('6','李键','男','18319729150','6'),('7','李光耀','男','154841212','7'),('8','郑程','女','784512165','8');
/*!40000 ALTER TABLE `agency` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add student info',7,'add_studentinfo'),(26,'Can change student info',7,'change_studentinfo'),(27,'Can delete student info',7,'delete_studentinfo'),(28,'Can view student info',7,'view_studentinfo'),(29,'Can add agency',8,'add_agency'),(30,'Can change agency',8,'change_agency'),(31,'Can delete agency',8,'delete_agency'),(32,'Can view agency',8,'view_agency'),(33,'Can add auth group',9,'add_authgroup'),(34,'Can change auth group',9,'change_authgroup'),(35,'Can delete auth group',9,'delete_authgroup'),(36,'Can view auth group',9,'view_authgroup'),(37,'Can add auth group permissions',10,'add_authgrouppermissions'),(38,'Can change auth group permissions',10,'change_authgrouppermissions'),(39,'Can delete auth group permissions',10,'delete_authgrouppermissions'),(40,'Can view auth group permissions',10,'view_authgrouppermissions'),(41,'Can add auth permission',11,'add_authpermission'),(42,'Can change auth permission',11,'change_authpermission'),(43,'Can delete auth permission',11,'delete_authpermission'),(44,'Can view auth permission',11,'view_authpermission'),(45,'Can add auth user',12,'add_authuser'),(46,'Can change auth user',12,'change_authuser'),(47,'Can delete auth user',12,'delete_authuser'),(48,'Can view auth user',12,'view_authuser'),(49,'Can add auth user groups',13,'add_authusergroups'),(50,'Can change auth user groups',13,'change_authusergroups'),(51,'Can delete auth user groups',13,'delete_authusergroups'),(52,'Can view auth user groups',13,'view_authusergroups'),(53,'Can add auth user user permissions',14,'add_authuseruserpermissions'),(54,'Can change auth user user permissions',14,'change_authuseruserpermissions'),(55,'Can delete auth user user permissions',14,'delete_authuseruserpermissions'),(56,'Can view auth user user permissions',14,'view_authuseruserpermissions'),(57,'Can add book',15,'add_book'),(58,'Can change book',15,'change_book'),(59,'Can delete book',15,'delete_book'),(60,'Can view book',15,'view_book'),(61,'Can add class',16,'add_class'),(62,'Can change class',16,'change_class'),(63,'Can delete class',16,'delete_class'),(64,'Can view class',16,'view_class'),(65,'Can add clinet',17,'add_clinet'),(66,'Can change clinet',17,'change_clinet'),(67,'Can delete clinet',17,'delete_clinet'),(68,'Can view clinet',17,'view_clinet'),(69,'Can add django admin log',18,'add_djangoadminlog'),(70,'Can change django admin log',18,'change_djangoadminlog'),(71,'Can delete django admin log',18,'delete_djangoadminlog'),(72,'Can view django admin log',18,'view_djangoadminlog'),(73,'Can add django content type',19,'add_djangocontenttype'),(74,'Can change django content type',19,'change_djangocontenttype'),(75,'Can delete django content type',19,'delete_djangocontenttype'),(76,'Can view django content type',19,'view_djangocontenttype'),(77,'Can add django migrations',20,'add_djangomigrations'),(78,'Can change django migrations',20,'change_djangomigrations'),(79,'Can delete django migrations',20,'delete_djangomigrations'),(80,'Can view django migrations',20,'view_djangomigrations'),(81,'Can add django session',21,'add_djangosession'),(82,'Can change django session',21,'change_djangosession'),(83,'Can delete django session',21,'delete_djangosession'),(84,'Can view django session',21,'view_djangosession'),(85,'Can add medicine',22,'add_medicine'),(86,'Can change medicine',22,'change_medicine'),(87,'Can delete medicine',22,'delete_medicine'),(88,'Can view medicine',22,'view_medicine'),(89,'Can add polls studentinfo',23,'add_pollsstudentinfo'),(90,'Can change polls studentinfo',23,'change_pollsstudentinfo'),(91,'Can delete polls studentinfo',23,'delete_pollsstudentinfo'),(92,'Can view polls studentinfo',23,'view_pollsstudentinfo'),(93,'Can add root',24,'add_root'),(94,'Can change root',24,'change_root'),(95,'Can delete root',24,'delete_root'),(96,'Can view root',24,'view_root'),(97,'Can add user',25,'add_user'),(98,'Can change user',25,'change_user'),(99,'Can delete user',25,'delete_user'),(100,'Can view user',25,'view_user');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$216000$hxmGjyPk0xFS$b0ssUVbtDA093eA4NugCHwIhebeL4cg8/sxj7U7ix3Q=','2020-10-20 07:26:00.966235',1,'sword','','','142755646@qq.com',1,1,'2020-10-20 07:24:51.816852');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `book`
--

DROP TABLE IF EXISTS `book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book` (
  `id` int NOT NULL,
  `title` varchar(45) DEFAULT NULL,
  `publisher` varchar(45) DEFAULT NULL,
  `introduce` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book`
--

LOCK TABLES `book` WRITE;
/*!40000 ALTER TABLE `book` DISABLE KEYS */;
INSERT INTO `book` VALUES (1,'python基础','中华人民出版社','大'),(2,'计算机网络','清华大学出版社','大'),(3,'C语言基础','清华大学出版社','大'),(4,'计算机基础','北京大小出版社','大'),(5,'数据科学','北京大学出版社','大'),(6,'数据结构','清华大学出版社','大'),(7,'Linux操作系统','清华大小出版社','大');
/*!40000 ALTER TABLE `book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `class`
--

DROP TABLE IF EXISTS `class`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `class` (
  `id` int NOT NULL,
  `class_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `class`
--

LOCK TABLES `class` WRITE;
/*!40000 ALTER TABLE `class` DISABLE KEYS */;
/*!40000 ALTER TABLE `class` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clinet`
--

DROP TABLE IF EXISTS `clinet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clinet` (
  `cno` char(10) NOT NULL,
  `cname` varchar(8) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `csex` char(1) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `cage` int DEFAULT NULL,
  `caddress` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `cphone` varchar(12) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `csymptom` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `mno` int DEFAULT NULL,
  `ano` char(8) DEFAULT NULL,
  `cdate` datetime DEFAULT NULL,
  `cremark` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `cmcount` int NOT NULL,
  PRIMARY KEY (`cno`),
  KEY `ano_idx` (`ano`),
  KEY `mno_idx` (`mno`),
  CONSTRAINT `ano` FOREIGN KEY (`ano`) REFERENCES `agency` (`ano`),
  CONSTRAINT `mno` FOREIGN KEY (`mno`) REFERENCES `medicine` (`mno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clinet`
--

LOCK TABLES `clinet` WRITE;
/*!40000 ALTER TABLE `clinet` DISABLE KEYS */;
INSERT INTO `clinet` VALUES ('1','李虎','男',21,'广东省肇庆市','14585612341','感冒',1,'1','2018-12-25 00:00:00','1',1),('2','黄洁','男',22,'广东省广州市','12324575212','感冒',3,'2','2018-12-02 00:00:00','2',1),('3','朱梦','女',21,'广东省肇庆市','12457896382','骨质疏松',10,'3','2018-12-15 00:00:00','3',1),('4','罗程','男',23,'广东省肇庆市','12345467757','胃溃疡',4,'4','2017-01-20 00:00:00','4',1),('5','张杰','男',31,'广东省广州市','12345685521','呼吸道感染',13,'5','2018-02-20 00:00:00','5',1),('6','罗伟鸣','男',44,'广东省肇庆市','12315662621','舌炎',8,'6','2018-11-20 00:00:00','6',1),('7','吴波','男',21,'广东省肇庆市','12345874562','消化不良',7,'7','2019-12-20 00:00:00','7',1);
/*!40000 ALTER TABLE `clinet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(8,'polls','agency'),(9,'polls','authgroup'),(10,'polls','authgrouppermissions'),(11,'polls','authpermission'),(12,'polls','authuser'),(13,'polls','authusergroups'),(14,'polls','authuseruserpermissions'),(15,'polls','book'),(16,'polls','class'),(17,'polls','clinet'),(18,'polls','djangoadminlog'),(19,'polls','djangocontenttype'),(20,'polls','djangomigrations'),(21,'polls','djangosession'),(22,'polls','medicine'),(23,'polls','pollsstudentinfo'),(24,'polls','root'),(7,'polls','studentinfo'),(25,'polls','user'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2020-10-20 07:01:51.559190'),(2,'auth','0001_initial','2020-10-20 07:01:51.918231'),(3,'admin','0001_initial','2020-10-20 07:01:53.083925'),(4,'admin','0002_logentry_remove_auto_add','2020-10-20 07:01:53.260871'),(5,'admin','0003_logentry_add_action_flag_choices','2020-10-20 07:01:53.271848'),(6,'contenttypes','0002_remove_content_type_name','2020-10-20 07:01:53.505223'),(7,'auth','0002_alter_permission_name_max_length','2020-10-20 07:01:53.648841'),(8,'auth','0003_alter_user_email_max_length','2020-10-20 07:01:53.700702'),(9,'auth','0004_alter_user_username_opts','2020-10-20 07:01:53.713667'),(10,'auth','0005_alter_user_last_login_null','2020-10-20 07:01:53.889242'),(11,'auth','0006_require_contenttypes_0002','2020-10-20 07:01:53.897221'),(12,'auth','0007_alter_validators_add_error_messages','2020-10-20 07:01:53.913178'),(13,'auth','0008_alter_user_username_max_length','2020-10-20 07:01:54.012911'),(14,'auth','0009_alter_user_last_name_max_length','2020-10-20 07:01:54.132102'),(15,'auth','0010_alter_group_name_max_length','2020-10-20 07:01:54.168519'),(16,'auth','0011_update_proxy_permissions','2020-10-20 07:01:54.186471'),(17,'auth','0012_alter_user_first_name_max_length','2020-10-20 07:01:54.312135'),(18,'sessions','0001_initial','2020-10-20 07:01:54.363001'),(19,'polls','0001_initial','2020-10-27 08:41:43.282391'),(20,'polls','0002_auto_20201117_2030','2020-11-17 12:31:05.230012'),(21,'polls','0003_auto_20201127_2139','2020-11-27 13:39:52.420751');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('ns0c22uzubg938r3ctluigz1t29n87t4','.eJxVjDsOwjAQRO_iGln-xYkp6XMGa727xgHkSHFSIe5OIqWAZop5b-YtImxriVvjJU4krkKLy2-XAJ9cD0APqPdZ4lzXZUryUORJmxxn4tftdP8OCrSyrz07JOM7p3vHmqizA_GeydqsOAXyVqHxyWkb0EA2iMiQjO0RBpWD-HwB7QQ4gg:1kUm1w:eP93fkAkgAl5IymItleoTAFPHz0p-g-UqAftbfjMR1M','2020-11-03 07:26:00.982192');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `medicine`
--

DROP TABLE IF EXISTS `medicine`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `medicine` (
  `mno` int NOT NULL,
  `mname` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `mmode` char(2) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `mefficacy` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `mcount` int DEFAULT NULL,
  PRIMARY KEY (`mno`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `medicine`
--

LOCK TABLES `medicine` WRITE;
/*!40000 ALTER TABLE `medicine` DISABLE KEYS */;
INSERT INTO `medicine` VALUES (1,'三九感冒灵','内服','治感冒',669),(2,'阿司匹林','内服','镇痛',9),(3,'感冒清热颗粒','内服','治感冒',1),(4,'斯达舒','内服','治胃溃疡',667),(5,'三九感冒灵','内服','消炎止痛，理气健胃',1),(6,'水溶性维生素','外用','补充水溶性维生素',1),(7,'维生素B1片','内服','脚气病、神经炎、消化不良等',667),(8,'维生素B2片','内服','角炎、唇干裂、舌炎',1),(9,'维生素B6片 ','内服','用于减轻妊娠呕吐',1),(10,'依普黄酮片','内服','骨质疏松',1),(12,'消炎止咳片','内服','消炎、镇咳、化痰',1),(13,'消炎片','内服','抗菌消炎，用于呼吸道感染',1);
/*!40000 ALTER TABLE `medicine` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `root`
--

DROP TABLE IF EXISTS `root`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `root` (
  `rootname` varchar(45) NOT NULL,
  `rootpassword` int NOT NULL,
  PRIMARY KEY (`rootname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `root`
--

LOCK TABLES `root` WRITE;
/*!40000 ALTER TABLE `root` DISABLE KEYS */;
INSERT INTO `root` VALUES ('root',123456);
/*!40000 ALTER TABLE `root` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `username` varchar(45) NOT NULL,
  `userphone` char(12) NOT NULL,
  `password` char(20) NOT NULL,
  `userid` varchar(45) NOT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('叶文','2144511222','123456','agency'),('李华一','15248482121','1213456','agency'),('李四','18814313032','123456789','purchaser'),('梁金海','15814313034','123456','agency'),('罗澄','15841151512','123456','purchaser'),('黄三','12345584451','1234','agency');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-07  9:28:13
