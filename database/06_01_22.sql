-- MySQL dump 10.13  Distrib 8.0.24, for Win64 (x86_64)
--
-- Host: localhost    Database: store
-- ------------------------------------------------------
-- Server version	8.0.24

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `inventory`
--

DROP TABLE IF EXISTS `inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventory` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Product_Name` varchar(100) NOT NULL,
  `stock` int NOT NULL,
  `cp` int DEFAULT NULL,
  `sp` int DEFAULT NULL,
  `totalcp` int DEFAULT NULL,
  `totalsp` int DEFAULT NULL,
  `assumed_profit` int DEFAULT NULL,
  `Vender` varchar(100) DEFAULT NULL,
  `date` varchar(12) DEFAULT NULL,
  `time` varchar(12) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory`
--

LOCK TABLES `inventory` WRITE;
/*!40000 ALTER TABLE `inventory` DISABLE KEYS */;
INSERT INTO `inventory` VALUES (1,'Octance_Pen',110,8,10,880,1100,220,'Classmate','29.11.2021','11:00:00'),(2,'KitKat',101,20,25,2240,2800,560,'Nestle','29.11.2021','11:00:00'),(3,'PenDrive_16',50,350,400,17500,20000,2500,'SONY','29.11.2021','11:00:00'),(4,'Boltt BH1400_headphone',40,1300,1500,52000,60000,8000,'BOLTT','29.11.2021','11:00:00'),(5,'Mighty Bottle 750mL',44,80,100,4000,5000,1000,'Mighty','29.11.2021','11:00:00'),(6,'Surgical Mask',113,4,5,480,600,120,'xyz','29.11.2021','11:00:00'),(7,'N95 Mask',92,40,45,4000,4500,500,'SWASA','29.11.2021','11:00:00'),(8,'Lays_HotnSweetChilli',60,17,20,1020,1200,180,'lays','29.11.2021','11:00:00'),(9,'Battey-AAA',48,8,10,384,480,96,'EVERYDAY','29.11.2021','11:00:00'),(10,'Notebook_24x18',40,45,50,2250,2500,250,'Classmate','29.11.2021','11:00:00'),(11,'Apsara_Plt_pencil',50,45,50,2250,2500,250,'Apsara','29.11.2021','11:00:00'),(12,'DairyMilk_nuts',48,70,80,43820,50080,6260,'Cadbury','29.11.2021','11:00:00'),(13,'adidas_shoe',40,550,600,22000,24000,2000,'Adidas','29.11.2021','11:00:00'),(14,'Lays_cream&onion',50,17,20,850,1000,150,'Lays','29.11.2021','11:00:00'),(15,'lock_6lvl',35,40,50,1400,1750,350,'Godrej','29.11.2021','11:00:00'),(16,'powerbank_20000',35,1470,1500,51450,52500,1050,'Coolnut','29.11.2021','11:00:00'),(17,'SSD_1tb',30,10000,12000,300000,360000,60000,'Sandisk','29.11.2021','11:00:00'),(18,'stapler ',50,40,50,2000,2500,500,'Kangaro','29.11.2021','11:00:00'),(19,'school_bag',50,600,800,30000,40000,10000,'Skybags','29.11.2021','11:00:00'),(20,'Ruler_30',34,13,15,455,525,70,'Khyati','29.11.2021','11:00:00'),(21,'paper_weight',35,170,200,5950,7000,1050,'Godrej','29.11.2021','11:00:00'),(22,'leatherJacket',30,5000,6000,150000,180000,30000,'Cobb','29.11.2021','11:00:00'),(23,'HDD_2tb',30,6000,7000,180000,210000,30000,'Seagate','29.11.2021','11:00:00'),(24,'card_reader',38,130,150,5200,6000,800,'Enter','29.11.2021','11:00:00'),(25,'cadbury_silk',90,60,80,6000,8000,2000,'Cadbury','29.11.2021','12:10:04'),(26,'lead_pencil',35,25,30,875,1050,175,'Camlin','29.11.2021','12:22:16'),(27,'ClassXII_bookset',20,550,600,16500,18000,1500,'NCERT','30.11.2021','12:11:15'),(28,'Liquid_handwash',50,90,100,4500,5000,500,'Dettol','30.11.2021','15:05:11'),(29,'360_ruler',30,22,25,660,750,90,'Maped','07.12.2021','17:52:10'),(30,'marker_pen',30,18,20,540,600,60,'Camlin','07.12.2021','17:52:33'),(31,'physics_notes',50,80,100,4000,5000,1000,'physics','07.12.2021','17:53:36'),(32,'mosquito_bat',19,90,100,1800,2000,200,'Onlite','07.12.2021','22:40:45'),(33,'tennis_ball',50,28,30,1400,1500,100,'Sg','08.12.2021','10:13:06'),(34,'Home_Cusion',30,90,100,2700,3000,300,'Homie','08.12.2021','14:42:17'),(35,'usbC_cable',30,270,300,8100,9000,900,'Samsung','08.12.2021','14:42:55'),(36,'body_lotion121',50,460,500,23000,25000,2000,'Nivea','08.12.2021','14:43:49'),(37,'newspaper',100,3,4,300,400,100,'Indian_Express','08.12.2021','14:44:24'),(38,'Geometry_box',30,200,220,6000,6600,600,'Maped','15.12.2021','08:14:27'),(39,'marker_red',50,17,20,850,1000,150,'Camlin','15.12.2021','08:27:27'),(40,'marker_violet',40,17,20,680,800,120,'Camlin','15.12.2021','08:30:03'),(41,'pencil_0.7mm',50,27,30,1350,1500,150,'Camlin','16.12.2021','10:30:28'),(42,'Shampoo_10',48,80,90,4000,4500,500,'Dove','17.12.2021','16:14:15'),(43,'Shampoo_12',100,175,190,17500,19000,1500,'Dove','17.12.2021','14:29:20'),(44,'Shampoo_13',50,170,185,8500,9250,750,'Pantene','17.12.2021','15:35:12'),(45,'shampoo_14',50,185,200,9250,10000,750,'Himalaya','17.12.2021','15:35:41'),(46,'Soap_01',30,40,45,1200,1350,150,'Santoor','17.12.2021','15:50:07'),(47,'Soap_02',35,55,60,1925,2100,175,'Nivea_Men','17.12.2021','15:50:33'),(48,'Soap_03',40,65,75,2600,3000,400,'Pears','17.12.2021','15:51:09'),(49,'Soap_04',30,70,80,2100,2400,300,'Flame','17.12.2021','15:51:56'),(50,'Lays_Spicy',49,17,20,850,1000,150,'Lays','18.12.2021','19:49:12'),(51,'Lays_ClassicSalt',100,8,10,800,1000,200,'Lays','17.12.2021','15:52:47'),(52,'Lays_Tomato',80,26,30,2080,2400,320,'Lays','24.12.2021','16:19:01'),(53,'Lays_MagicMasala',100,25,30,2500,3000,500,'Lays','17.12.2021','15:53:59'),(54,'PenDrive_32',50,650,700,32500,35000,2500,'Sony','17.12.2021','16:18:12'),(55,'Study_lamp',45,470,500,21150,22500,1350,'Akari','18.12.2021','08:24:50'),(56,'wallet',25,480,500,9600,10000,400,'Genuine_Leather','01.01.2022','13:04:12'),(57,'wallet_G',20,480,500,9600,10000,400,'Genuine_Leather','25.12.2021','12:43:53'),(58,'Salt_Chips',50,17,20,850,1000,150,'Bingo','25.12.2021','13:34:52'),(59,'Tomato_chips',20,17,20,340,400,60,'Bingo','25.12.2021','14:03:19'),(60,'Masala_Chips',30,16,20,480,600,120,'Bingo','28.12.2021','12:25:05'),(61,'special_chips',30,35,40,1050,1200,150,'Bingo','02.01.2022','09:58:25');
/*!40000 ALTER TABLE `inventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transactions`
--

DROP TABLE IF EXISTS `transactions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transactions` (
  `ID` int DEFAULT NULL,
  `Product_Name` varchar(100) DEFAULT NULL,
  `Quantity` int DEFAULT NULL,
  `Received_Amount` int DEFAULT NULL,
  `bill_profit` int DEFAULT NULL,
  `date` varchar(12) DEFAULT NULL,
  `time` varchar(12) DEFAULT NULL,
  `invoice` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transactions`
--

LOCK TABLES `transactions` WRITE;
/*!40000 ALTER TABLE `transactions` DISABLE KEYS */;
INSERT INTO `transactions` VALUES (1,'Octance_Pen',1,10,219,'01.01.2022','00:47:54',1056),(2,'KitKat',1,25,219,'01.01.2022','00:47:54',1056),(3,'PenDrive_16',1,400,219,'01.01.2022','00:47:54',1056),(4,'Boltt BH1400_headphone',1,1500,219,'01.01.2022','00:47:54',1056),(11,'Apsara_Plt_pencil',1,50,31,'01.01.2022','00:50:54',1057),(12,'DairyMilk_nuts',1,80,31,'01.01.2022','00:50:54',1057),(24,'card_reader',1,150,31,'01.01.2022','00:50:54',1057),(1,'Octance_Pen',1,10,2,'01.01.2022','00:57:15',1058),(1,'Octance_Pen',1,10,1,'01.01.2022','08:46:53',1059),(1,'Octance_Pen',1,10,2,'01.01.2022','08:59:35',1064),(42,'Shampoo_10',1,90,10,'01.01.2022','09:10:19',1068),(55,'Study_lamp',1,500,30,'01.01.2022','09:14:02',1069),(2,'KitKat',1,25,5,'01.01.2022','09:57:43',1071),(2,'KitKat',1,25,5,'01.01.2022','09:58:22',1072),(1,'Octance_Pen',1,10,10,'01.01.2022','13:03:45',1073),(42,'Shampoo_10',1,90,10,'01.01.2022','13:03:45',1073),(62,'testme',1,10,2,'02.01.2022','10:20:31',1074),(1,'Octance_Pen',1,10,1,'05.01.2022','07:40:22',1075),(1,'Octance_Pen',1,10,1,'05.01.2022','21:17:47',1076),(1,'Octance_Pen',1,10,2,'05.01.2022','22:51:08',1078),(5,'Mighty Bottle 750mL',1,100,20,'05.01.2022','23:09:32',1079),(6,'Surgical Mask',1,5,6,'05.01.2022','23:24:40',1080),(7,'N95 Mask',1,45,6,'05.01.2022','23:24:40',1080),(12,'DairyMilk_nuts',1,80,48,'05.01.2022','23:30:06',1081),(50,'Lays_Spicy',1,20,48,'05.01.2022','23:30:06',1081),(2,'KitKat',2,50,48,'05.01.2022','23:30:06',1081),(61,'special_chips',1,40,48,'05.01.2022','23:30:06',1081),(8,'Lays_HotnSweetChilli',1,20,3,'06.01.2022','09:55:40',1082),(9,'Battey-AAA',1,10,2,'06.01.2022','10:27:01',1083),(9,'Battey-AAA',1,10,2,'06.01.2022','10:43:30',1084);
/*!40000 ALTER TABLE `transactions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-01-06 11:14:50
