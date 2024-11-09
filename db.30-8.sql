/*
SQLyog Community v13.1.5  (64 bit)
MySQL - 8.0.33 : Database - bookstore
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`bookstore` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `bookstore`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add book',7,'add_book'),
(26,'Can change book',7,'change_book'),
(27,'Can delete book',7,'delete_book'),
(28,'Can view book',7,'view_book'),
(29,'Can add category',8,'add_category'),
(30,'Can change category',8,'change_category'),
(31,'Can delete category',8,'delete_category'),
(32,'Can view category',8,'view_category'),
(33,'Can add login',9,'add_login'),
(34,'Can change login',9,'change_login'),
(35,'Can delete login',9,'delete_login'),
(36,'Can view login',9,'view_login'),
(37,'Can add user',10,'add_user'),
(38,'Can change user',10,'change_user'),
(39,'Can delete user',10,'delete_user'),
(40,'Can view user',10,'view_user'),
(41,'Can add review',11,'add_review'),
(42,'Can change review',11,'change_review'),
(43,'Can delete review',11,'delete_review'),
(44,'Can view review',11,'view_review'),
(45,'Can add order',12,'add_order'),
(46,'Can change order',12,'change_order'),
(47,'Can delete order',12,'delete_order'),
(48,'Can view order',12,'view_order'),
(49,'Can add feedback',13,'add_feedback'),
(50,'Can change feedback',13,'change_feedback'),
(51,'Can delete feedback',13,'delete_feedback'),
(52,'Can view feedback',13,'view_feedback'),
(53,'Can add complaints',14,'add_complaints'),
(54,'Can change complaints',14,'change_complaints'),
(55,'Can delete complaints',14,'delete_complaints'),
(56,'Can view complaints',14,'view_complaints'),
(57,'Can add bill_details',15,'add_bill_details'),
(58,'Can change bill_details',15,'change_bill_details'),
(59,'Can delete bill_details',15,'delete_bill_details'),
(60,'Can view bill_details',15,'view_bill_details'),
(61,'Can add bill',16,'add_bill'),
(62,'Can change bill',16,'change_bill'),
(63,'Can delete bill',16,'delete_bill'),
(64,'Can view bill',16,'view_bill');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

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

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(16,'myapp','bill'),
(15,'myapp','bill_details'),
(7,'myapp','book'),
(8,'myapp','category'),
(14,'myapp','complaints'),
(13,'myapp','feedback'),
(9,'myapp','login'),
(12,'myapp','order'),
(11,'myapp','review'),
(10,'myapp','user'),
(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2024-08-30 09:14:23.000978'),
(2,'auth','0001_initial','2024-08-30 09:14:23.510650'),
(3,'admin','0001_initial','2024-08-30 09:14:23.618034'),
(4,'admin','0002_logentry_remove_auto_add','2024-08-30 09:14:23.630049'),
(5,'admin','0003_logentry_add_action_flag_choices','2024-08-30 09:14:23.665159'),
(6,'contenttypes','0002_remove_content_type_name','2024-08-30 09:14:23.731865'),
(7,'auth','0002_alter_permission_name_max_length','2024-08-30 09:14:23.786941'),
(8,'auth','0003_alter_user_email_max_length','2024-08-30 09:14:23.820707'),
(9,'auth','0004_alter_user_username_opts','2024-08-30 09:14:23.832683'),
(10,'auth','0005_alter_user_last_login_null','2024-08-30 09:14:23.887278'),
(11,'auth','0006_require_contenttypes_0002','2024-08-30 09:14:23.892774'),
(12,'auth','0007_alter_validators_add_error_messages','2024-08-30 09:14:23.901814'),
(13,'auth','0008_alter_user_username_max_length','2024-08-30 09:14:23.954126'),
(14,'auth','0009_alter_user_last_name_max_length','2024-08-30 09:14:24.015280'),
(15,'auth','0010_alter_group_name_max_length','2024-08-30 09:14:24.044272'),
(16,'auth','0011_update_proxy_permissions','2024-08-30 09:14:24.055265'),
(17,'auth','0012_alter_user_first_name_max_length','2024-08-30 09:14:24.126329'),
(18,'myapp','0001_initial','2024-08-30 09:14:24.789458'),
(19,'myapp','0002_remove_book_login','2024-08-30 09:14:24.871403'),
(20,'myapp','0003_book_title','2024-08-30 09:14:24.915944'),
(21,'sessions','0001_initial','2024-08-30 09:17:50.589456'),
(22,'myapp','0002_book_adddate','2024-08-30 09:53:05.644810'),
(23,'myapp','0003_user_registerationdate','2024-08-30 10:09:55.383605');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('blaa0k2smlam7gsc7qtmabumdk1f5i53','.eJyrVkrKz89WsjLWUSotTi1SsjLQUUpOLFGyMtJRyklMUrKKVjIyMDJS0gFRxhDKRClWRyklsSQRKGuoA4SxEM3xEA0wHlRFbC0AOUobvA:1sjydS:VghWm5r5VLIfWk8Vi5gWDfX5G5dDisObiploFa8SOBc','2024-09-13 10:13:42.680593'),
('mrogzczc1qb6d6xwt6rn9g4gd6oiyjcm','.eJxFTDsOgCAUu0vnNwg4cRVDzAMciChGcTLeXYQY06Hp90IMHloSbEoztCKcx7RDC4LjXJPIFnqA7KQEvaQa9TAEz5lLKqjAtPH4D2qlel-vaJeWLXJYy3t3P60RI7A:1sjyoD:AijRfHqKfll9PDmZap5DpaCqSc9-9cOUS3Z_optWaEw','2024-09-13 10:24:49.875980');

/*Table structure for table `myapp_bill` */

DROP TABLE IF EXISTS `myapp_bill`;

CREATE TABLE `myapp_bill` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `amount` double NOT NULL,
  `date` date NOT NULL,
  `status` varchar(20) NOT NULL,
  `Type` varchar(100) NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_bill_USER_id_20ed8466_fk_myapp_user_id` (`USER_id`),
  CONSTRAINT `myapp_bill_USER_id_20ed8466_fk_myapp_user_id` FOREIGN KEY (`USER_id`) REFERENCES `myapp_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_bill` */

/*Table structure for table `myapp_bill_details` */

DROP TABLE IF EXISTS `myapp_bill_details`;

CREATE TABLE `myapp_bill_details` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `quantity` int NOT NULL,
  `BOOK_id` bigint NOT NULL,
  `ORDER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_bill_details_BOOK_id_8394eb81_fk_myapp_book_id` (`BOOK_id`),
  KEY `myapp_bill_details_ORDER_id_e16349b6_fk_myapp_order_id` (`ORDER_id`),
  CONSTRAINT `myapp_bill_details_BOOK_id_8394eb81_fk_myapp_book_id` FOREIGN KEY (`BOOK_id`) REFERENCES `myapp_book` (`id`),
  CONSTRAINT `myapp_bill_details_ORDER_id_e16349b6_fk_myapp_order_id` FOREIGN KEY (`ORDER_id`) REFERENCES `myapp_order` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_bill_details` */

/*Table structure for table `myapp_book` */

DROP TABLE IF EXISTS `myapp_book`;

CREATE TABLE `myapp_book` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `price` double NOT NULL,
  `quantity` int NOT NULL,
  `author` varchar(20) NOT NULL,
  `publish_year` date NOT NULL,
  `language` varchar(100) NOT NULL,
  `publisher` varchar(100) NOT NULL,
  `image` varchar(400) NOT NULL,
  `description` varchar(400) NOT NULL,
  `CATEGORY_id` bigint NOT NULL,
  `title` varchar(20) NOT NULL,
  `adddate` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_book_CATEGORY_id_b1dd7407_fk_myapp_category_id` (`CATEGORY_id`),
  CONSTRAINT `myapp_book_CATEGORY_id_b1dd7407_fk_myapp_category_id` FOREIGN KEY (`CATEGORY_id`) REFERENCES `myapp_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_book` */

insert  into `myapp_book`(`id`,`price`,`quantity`,`author`,`publish_year`,`language`,`publisher`,`image`,`description`,`CATEGORY_id`,`title`,`adddate`) values 
(1,20,2,'dsd','2024-08-07','malayalam','ok','/media/2024-08-30-15-03-51.jpg','sadf',1,'erewrew','2024'),
(2,20,2,'dsd','2024-08-30','malayalam','ok','/media/2024-08-30-15-16-27.jpg','sas',1,'hkh','2022'),
(3,20,2,'dsd','2024-08-16','malayalam','ok','/media/2024-08-30-15-24-18.jpg','sqdwd',1,'hkhsqsq','2023'),
(4,19.99,10,'Brett Slatkin','2019-03-07','English','Addison-Wesley','http://example.com/effective_python.jpg','A guide to Python programming with tips and best practices.',1,'Effective Python','2024-08-30'),
(5,15.99,20,'George Orwell','1949-06-08','English','Secker & Warburg','http://example.com/1984.jpg','A dystopian social science fiction novel and cautionary tale.',2,'1984','2024-08-30'),
(6,12.99,30,'F. Scott Fitzgerald','1925-04-10','English','Charles Scribner\'s Sons','http://example.com/the_great_gatsby.jpg','A critique of the American Dream during the Jazz Age.',3,'The Great Gatsby','2024-08-30'),
(7,17.99,25,'Herman Melville','1851-10-18','English','Harper & Brothers','http://example.com/moby_dick.jpg','A novel about the voyage of the whaling ship Pequod.',5,'Moby Dick','2024-08-30'),
(8,9.99,35,'Jane Austen','1813-01-28','English','T. Egerton','http://example.com/pride_and_prejudice.jpg','A romantic novel that also critiques the British landed gentry.',7,'Pride and Prejudice','2024-08-30'),
(9,19.99,50,'J.R.R. Tolkien','1937-09-21','English','George Allen & Unwin','http://example.com/the_hobbit.jpg','A fantasy novel that precedes Tolkien’s Lord of the Rings.',8,'The Hobbit','2024-08-30'),
(10,24.99,45,'Leo Tolstoy','1869-03-01','Russian','The Russian Messenger','http://example.com/war_and_peace.jpg','A historical novel that covers the French invasion of Russia.',9,'War and Peace','2024-08-30'),
(11,19.99,60,'Dan Brown','2003-03-18','English','Doubleday','http://example.com/the_da_vinci_code.jpg','A thriller that delves into art, religion, and conspiracy.',10,'The Da Vinci Code','2024-08-30'),
(12,19.99,60,'Dan Brown','2003-03-18','English','Doubleday','http://example.com/the_da_vinci_code.jpg','A thriller that delves into art, religion, and conspiracy.',10,'The Da Vinci Code','2024-08-30'),
(13,21.99,70,'Aldous Huxley','1932-08-30','English','Chatto & Windus','http://example.com/brave_new_world.jpg','A dystopian novel set in a futuristic world.',11,'Brave New World','2024-08-30'),
(14,25.99,55,'Ray Bradbury','1953-10-19','English','Ballantine Books','http://example.com/fahrenheit_451.jpg','A novel about a future society where books are banned.',12,'Fahrenheit 451','2024-08-30'),
(15,16.99,80,'Joseph Heller','1961-11-10','English','Simon & Schuster','http://example.com/catch_22.jpg','A satirical novel about the absurdities of war.',13,'Catch-22','2024-08-30');

/*Table structure for table `myapp_category` */

DROP TABLE IF EXISTS `myapp_category`;

CREATE TABLE `myapp_category` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `category` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_category` */

insert  into `myapp_category`(`id`,`category`) values 
(1,'Novel'),
(2,'Poetry'),
(3,'Mystery'),
(4,'History'),
(5,'Horror'),
(6,'Political thriller'),
(7,'Romance'),
(8,'Young adult'),
(9,'Thriller'),
(10,'Short story'),
(11,'Drama'),
(12,'Crime'),
(13,'Comics'),
(14,'Classic'),
(15,'Children\'s'),
(16,'Action and adventure');

/*Table structure for table `myapp_complaints` */

DROP TABLE IF EXISTS `myapp_complaints`;

CREATE TABLE `myapp_complaints` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `complaints` varchar(400) NOT NULL,
  `date` date NOT NULL,
  `reply` varchar(400) NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_complaints_USER_id_f1892848_fk_myapp_user_id` (`USER_id`),
  CONSTRAINT `myapp_complaints_USER_id_f1892848_fk_myapp_user_id` FOREIGN KEY (`USER_id`) REFERENCES `myapp_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_complaints` */

/*Table structure for table `myapp_feedback` */

DROP TABLE IF EXISTS `myapp_feedback`;

CREATE TABLE `myapp_feedback` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `feedback` varchar(20) NOT NULL,
  `BOOK_id` bigint NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_feedback_BOOK_id_bfc83236_fk_myapp_book_id` (`BOOK_id`),
  KEY `myapp_feedback_USER_id_fce7ccff_fk_myapp_user_id` (`USER_id`),
  CONSTRAINT `myapp_feedback_BOOK_id_bfc83236_fk_myapp_book_id` FOREIGN KEY (`BOOK_id`) REFERENCES `myapp_book` (`id`),
  CONSTRAINT `myapp_feedback_USER_id_fce7ccff_fk_myapp_user_id` FOREIGN KEY (`USER_id`) REFERENCES `myapp_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_feedback` */

/*Table structure for table `myapp_login` */

DROP TABLE IF EXISTS `myapp_login`;

CREATE TABLE `myapp_login` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `type` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_login` */

insert  into `myapp_login`(`id`,`username`,`password`,`type`) values 
(1,'user@gmail.com','12345678','user'),
(2,'admin','admin','admin');

/*Table structure for table `myapp_order` */

DROP TABLE IF EXISTS `myapp_order`;

CREATE TABLE `myapp_order` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `price` double NOT NULL,
  `date` date NOT NULL,
  `place` varchar(20) NOT NULL,
  `pin` varchar(20) NOT NULL,
  `landmark` varchar(20) NOT NULL,
  `address` varchar(20) NOT NULL,
  `status` varchar(20) NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_order_USER_id_5a79bc4c_fk_myapp_user_id` (`USER_id`),
  CONSTRAINT `myapp_order_USER_id_5a79bc4c_fk_myapp_user_id` FOREIGN KEY (`USER_id`) REFERENCES `myapp_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_order` */

/*Table structure for table `myapp_review` */

DROP TABLE IF EXISTS `myapp_review`;

CREATE TABLE `myapp_review` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `review` varchar(20) NOT NULL,
  `rating` varchar(20) NOT NULL,
  `BOOK_id` bigint NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_review_BOOK_id_82ed191b_fk_myapp_book_id` (`BOOK_id`),
  KEY `myapp_review_USER_id_0e923f15_fk_myapp_user_id` (`USER_id`),
  CONSTRAINT `myapp_review_BOOK_id_82ed191b_fk_myapp_book_id` FOREIGN KEY (`BOOK_id`) REFERENCES `myapp_book` (`id`),
  CONSTRAINT `myapp_review_USER_id_0e923f15_fk_myapp_user_id` FOREIGN KEY (`USER_id`) REFERENCES `myapp_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_review` */

/*Table structure for table `myapp_user` */

DROP TABLE IF EXISTS `myapp_user`;

CREATE TABLE `myapp_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fname` varchar(100) NOT NULL,
  `lname` varchar(100) NOT NULL,
  `gender` varchar(20) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phonenumber` bigint NOT NULL,
  `image` varchar(400) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  `registerationdate` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `myapp_user_LOGIN_id_da832ded_fk_myapp_login_id` (`LOGIN_id`),
  CONSTRAINT `myapp_user_LOGIN_id_da832ded_fk_myapp_login_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `myapp_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `myapp_user` */

insert  into `myapp_user`(`id`,`fname`,`lname`,`gender`,`email`,`phonenumber`,`image`,`LOGIN_id`,`registerationdate`) values 
(1,'user','name','male','user@gmail.com',9874563210,'/media/2024-08-30-15-46-43.jpg',1,'2024');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
