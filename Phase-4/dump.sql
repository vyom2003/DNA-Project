-- MySQL dump 10.13  Distrib 8.0.31, for Linux (x86_64)
--
-- Host: localhost    Database: project_6
-- ------------------------------------------------------
-- Server version	8.0.31-0ubuntu0.20.04.1

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
-- Table structure for table `Bank_account`
--

DROP TABLE IF EXISTS `Bank_account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Bank_account` (
  `Account_number` bigint NOT NULL,
  `Name_of_holder` varchar(50) DEFAULT NULL,
  `Account_type` varchar(20) DEFAULT NULL,
  `Current_balance` int DEFAULT NULL,
  `Branch_IFSC` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Account_number`),
  KEY `Branch_IFSC` (`Branch_IFSC`),
  CONSTRAINT `Bank_account_ibfk_1` FOREIGN KEY (`Branch_IFSC`) REFERENCES `Banks` (`Branch_IFSC`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Bank_account`
--

LOCK TABLES `Bank_account` WRITE;
/*!40000 ALTER TABLE `Bank_account` DISABLE KEYS */;
INSERT INTO `Bank_account` VALUES (987654321,'Vyom','Savings',647647,'BOB1234'),(1234567890,'Aarnav','Current',787283,'SBI1234'),(2345678901,'Nipun','Current',73232283,'YES1234'),(3456789012,'Gaurav','Current',625372,'BOB1234'),(4567890123,'Vinkesh','Savings',1,'HDFC1234'),(5432109876,'Rhythm','Current',11323123,'HDFC1234'),(6543210987,'Khushi','Current',3243244,'BOB1234'),(7654321098,'Kabir','Savings',323332,'SBI1234'),(8765432190,'Nipun','Savings',323322,'SBI1234');
/*!40000 ALTER TABLE `Bank_account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Banks`
--

DROP TABLE IF EXISTS `Banks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Banks` (
  `Branch_IFSC` varchar(50) NOT NULL,
  `Name_of_Bank` varchar(50) DEFAULT NULL,
  `Bank_Address` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Branch_IFSC`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Banks`
--

LOCK TABLES `Banks` WRITE;
/*!40000 ALTER TABLE `Banks` DISABLE KEYS */;
INSERT INTO `Banks` VALUES ('BOB1234','Bank_of_Baroda','Gachibowli'),('HDFC1234','HDFC','Connaught place'),('SBI1234','State_Bank_of_India','Chanakyapuri'),('YES1234','YES','Surat');
/*!40000 ALTER TABLE `Banks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Department`
--

DROP TABLE IF EXISTS `Department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Department` (
  `Dno` int NOT NULL,
  `Dname` varchar(20) DEFAULT NULL,
  `Manager_id` int DEFAULT NULL,
  PRIMARY KEY (`Dno`),
  CONSTRAINT `Department_ibfk_1` FOREIGN KEY (`Manager_id`) REFERENCES `Employee` (`Employee_id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Department`
--

LOCK TABLES `Department` WRITE;
/*!40000 ALTER TABLE `Department` DISABLE KEYS */;
INSERT INTO `Department` VALUES (1,'Finance',101),(2,'Administration',102),(3,'Marketing',103);
/*!40000 ALTER TABLE `Department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Department_Spendings`
--

DROP TABLE IF EXISTS `Department_Spendings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Department_Spendings` (
  `Department_Number` int NOT NULL,
  `Amount_Spend` int DEFAULT NULL,
  `Date_of_spend` date NOT NULL,
  `Description` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Department_Number`,`Date_of_spend`),
  CONSTRAINT `Department_Spendings_ibfk_1` FOREIGN KEY (`Department_Number`) REFERENCES `Department` (`Dno`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Department_Spendings`
--

LOCK TABLES `Department_Spendings` WRITE;
/*!40000 ALTER TABLE `Department_Spendings` DISABLE KEYS */;
INSERT INTO `Department_Spendings` VALUES (1,100000,'2022-03-23','Expenditure OK'),(2,200000,'2022-01-03','High Spendings'),(2,130000,'2022-05-14','Expenditure OK'),(3,150000,'2022-01-08','High Spendings');
/*!40000 ALTER TABLE `Department_Spendings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Distributors`
--

DROP TABLE IF EXISTS `Distributors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Distributors` (
  `Distributor_id` int NOT NULL,
  `Distributor_name` varchar(50) DEFAULT NULL,
  `Bank_Acc_no` bigint DEFAULT NULL,
  `IFSC` varchar(30) DEFAULT NULL,
  `Area_of_jurisdiction` varchar(30) DEFAULT NULL,
  `Yearly_Sales` int DEFAULT NULL,
  `Area_Salesman_id` int DEFAULT NULL,
  `Address` varchar(50) DEFAULT NULL,
  `Phone_No` bigint DEFAULT NULL,
  `GST` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Distributor_id`),
  KEY `Area_Salesman_id` (`Area_Salesman_id`),
  CONSTRAINT `Distributors_ibfk_1` FOREIGN KEY (`Area_Salesman_id`) REFERENCES `Employee` (`Employee_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Distributors`
--

LOCK TABLES `Distributors` WRITE;
/*!40000 ALTER TABLE `Distributors` DISABLE KEYS */;
INSERT INTO `Distributors` VALUES (1001,'Mohan',1122334455,'BOB1234','Hyderabad',10000000,107,'GB Road',1234567890,'ABC1234'),(1002,'Sitaram',2233445566,'YES1234','Bhopal',80000000,108,'Gachibowli',3456789012,'DEF1234'),(1003,'Kamal',3344556677,'SBI1234','Pune',22500000,109,'Madhapur',2345678901,'GHI1234'),(1004,'Venkatesh',4455667788,'HDFC1234','Indore',40000000,110,'Secundrabad',3456789012,'JKL1234');
/*!40000 ALTER TABLE `Distributors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Employee`
--

DROP TABLE IF EXISTS `Employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Employee` (
  `Employee_id` int NOT NULL,
  `Fname` varchar(50) DEFAULT NULL,
  `Lname` varchar(50) DEFAULT NULL,
  `Post` varchar(20) DEFAULT NULL,
  `Salary` int DEFAULT NULL,
  `Gender` varchar(5) DEFAULT NULL,
  `Address` varchar(50) DEFAULT NULL,
  `DOB` date DEFAULT NULL,
  `Acc_no` bigint DEFAULT NULL,
  `Manager_id` int DEFAULT NULL,
  PRIMARY KEY (`Employee_id`),
  KEY `Manager_id` (`Manager_id`),
  CONSTRAINT `Employee_ibfk_1` FOREIGN KEY (`Manager_id`) REFERENCES `Employee` (`Employee_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Employee`
--

LOCK TABLES `Employee` WRITE;
/*!40000 ALTER TABLE `Employee` DISABLE KEYS */;
INSERT INTO `Employee` VALUES (101,'Aman','Sharma','Manager',10000,'M','A street , Hyderabad','1998-12-14',3671263362,NULL),(102,'Vinkesh','Khothari','Manager',20000,'M','B street , Hyderabad','1999-12-03',5634637493,NULL),(103,'Rhythm','Khothari','Manager',332032,'M','Abc , delhi','1995-06-21',3847384738,NULL),(104,'Khushi','Khothari','junior employee',213123,'F','C street ,Delhi','1980-08-07',7834483748,NULL),(105,'Gaurav','Bansal','Senior employee',312312,'F','Building 2, Surat','1999-01-27',4349384934,NULL),(106,'Aarnav','Nageria','Senior employee',31282,'M','Building 3 , Surat','1989-08-12',8438394394,NULL),(107,'Kritika','Jautam','junior employee',227223,'F','Building 4, Surat','1986-07-21',8943898394,NULL),(108,'Mitansh','Muthyaal','Senior employee',23726372,'M','Jhopdi 1 , Delhi','1986-02-22',9993493490,NULL),(109,'Sanidya','Gupta','junior employee',3232323,'M','Jhopdi 2,Surat','1989-01-27',4343434344,NULL),(110,'Nipun','Maheswari','junior employee',6327328,'M','Jhopdi 3,Bhopal','2002-04-27',7844943948,NULL);
/*!40000 ALTER TABLE `Employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Employee_Family_details`
--

DROP TABLE IF EXISTS `Employee_Family_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Employee_Family_details` (
  `Employee_id` int NOT NULL,
  `FName` varchar(20) NOT NULL,
  `Lname` varchar(20) NOT NULL,
  `Relation` varchar(20) DEFAULT NULL,
  `DOB` date DEFAULT NULL,
  `Gender` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`Employee_id`,`FName`,`Lname`),
  CONSTRAINT `Employee_Family_details_ibfk_1` FOREIGN KEY (`Employee_id`) REFERENCES `Employee` (`Employee_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Employee_Family_details`
--

LOCK TABLES `Employee_Family_details` WRITE;
/*!40000 ALTER TABLE `Employee_Family_details` DISABLE KEYS */;
INSERT INTO `Employee_Family_details` VALUES (101,'Naman','Sharma','Bro','2002-03-19','M'),(101,'Sita','Sharma','Wife','1995-05-07','F'),(102,'Bhavya','Khotari','Father','1999-05-04','M'),(103,'Bhavya','Khotari','Father','1998-04-27','F'),(104,'Kirtika','Khotari','Mother','1994-09-04','F'),(105,'Aayush','Bansal','Father','1980-11-04','M'),(106,'Bharat','Nageria','Father','1980-07-03','M'),(107,'Kabir','Jautam','Husband','1990-01-27','M'),(108,'Mahika','Jain','Wife','1994-10-22','F'),(109,'Mahika','Gupta','Mother','1990-01-14','F'),(110,'Charu','Maheshwari','Wife','1989-02-24','F');
/*!40000 ALTER TABLE `Employee_Family_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Inventory`
--

DROP TABLE IF EXISTS `Inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Inventory` (
  `Item_number` int NOT NULL,
  `Item_name` varchar(50) DEFAULT NULL,
  `Availability` int DEFAULT NULL,
  `Profit` int DEFAULT NULL,
  `Mrp` float DEFAULT NULL,
  `Purchase_cost` float DEFAULT NULL,
  PRIMARY KEY (`Item_number`),
  CONSTRAINT `check_sum` CHECK (((`Purchase_cost` + `Profit`) = `Mrp`))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Inventory`
--

LOCK TABLES `Inventory` WRITE;
/*!40000 ALTER TABLE `Inventory` DISABLE KEYS */;
INSERT INTO `Inventory` VALUES (201,'Soap',1000,5,90,85),(202,'Dispensor',2000,8,150,142),(203,'Toothpaste',800,5,150,145),(204,'Bodywash',250,20,100,80);
/*!40000 ALTER TABLE `Inventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Loan`
--

DROP TABLE IF EXISTS `Loan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Loan` (
  `Loan_id` int NOT NULL,
  `Provider` bigint DEFAULT NULL,
  `Principal_amt` int DEFAULT NULL,
  `Interest_charge` int DEFAULT NULL,
  `Collateral` varchar(1000) DEFAULT NULL,
  `Loan_tenure` int DEFAULT NULL,
  `Loan_approval_date` date DEFAULT NULL,
  `Installments` int DEFAULT NULL,
  PRIMARY KEY (`Loan_id`),
  KEY `Provider` (`Provider`),
  CONSTRAINT `Loan_ibfk_1` FOREIGN KEY (`Provider`) REFERENCES `Bank_account` (`Account_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Loan`
--

LOCK TABLES `Loan` WRITE;
/*!40000 ALTER TABLE `Loan` DISABLE KEYS */;
INSERT INTO `Loan` VALUES (501,987654321,10000000,0,'Home',1,'2022-04-04',6),(502,8765432190,500000,0,'Car',2,'2022-05-09',4),(503,7654321098,1500000,0,'Gold',1,'2022-02-12',5),(504,6543210987,100000000,0,'Home',3,'2022-05-30',6),(505,5432109876,120000000,0,'Home',4,'2022-01-02',6);
/*!40000 ALTER TABLE `Loan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Loan_Takers`
--

DROP TABLE IF EXISTS `Loan_Takers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Loan_Takers` (
  `Loan_id` int NOT NULL,
  `Employee_id` int DEFAULT NULL,
  `Owner_id` int DEFAULT NULL,
  PRIMARY KEY (`Loan_id`),
  KEY `Owner_id` (`Owner_id`),
  KEY `Employee_id` (`Employee_id`),
  CONSTRAINT `Loan_Takers_ibfk_1` FOREIGN KEY (`Owner_id`) REFERENCES `Owner` (`Owner_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Loan_Takers_ibfk_2` FOREIGN KEY (`Employee_id`) REFERENCES `Employee` (`Employee_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Loan_Takers`
--

LOCK TABLES `Loan_Takers` WRITE;
/*!40000 ALTER TABLE `Loan_Takers` DISABLE KEYS */;
INSERT INTO `Loan_Takers` VALUES (501,101,NULL),(502,NULL,1),(503,NULL,2),(504,107,NULL),(505,108,NULL);
/*!40000 ALTER TABLE `Loan_Takers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Monitors`
--

DROP TABLE IF EXISTS `Monitors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Monitors` (
  `Order_no` int NOT NULL,
  `Distributor_id` int NOT NULL,
  `Employee_id` int NOT NULL,
  `Owner_id` int NOT NULL,
  PRIMARY KEY (`Order_no`,`Distributor_id`,`Employee_id`,`Owner_id`),
  KEY `Distributor_id` (`Distributor_id`),
  KEY `Owner_id` (`Owner_id`),
  KEY `Employee_id` (`Employee_id`),
  CONSTRAINT `Monitors_ibfk_1` FOREIGN KEY (`Order_no`) REFERENCES `Orders` (`Order_no`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Monitors_ibfk_2` FOREIGN KEY (`Distributor_id`) REFERENCES `Distributors` (`Distributor_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Monitors_ibfk_3` FOREIGN KEY (`Owner_id`) REFERENCES `Owner` (`Owner_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Monitors_ibfk_4` FOREIGN KEY (`Employee_id`) REFERENCES `Employee` (`Employee_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Monitors`
--

LOCK TABLES `Monitors` WRITE;
/*!40000 ALTER TABLE `Monitors` DISABLE KEYS */;
INSERT INTO `Monitors` VALUES (121,1001,104,3),(122,1002,105,2),(123,1003,106,1),(124,1004,103,2);
/*!40000 ALTER TABLE `Monitors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Order_Description`
--

DROP TABLE IF EXISTS `Order_Description`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Order_Description` (
  `Order_no` int NOT NULL,
  `Product_no` int NOT NULL,
  `Quantity` int DEFAULT NULL,
  PRIMARY KEY (`Order_no`,`Product_no`),
  KEY `Product_no` (`Product_no`),
  CONSTRAINT `Order_Description_ibfk_1` FOREIGN KEY (`Order_no`) REFERENCES `Orders` (`Order_no`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Order_Description_ibfk_2` FOREIGN KEY (`Product_no`) REFERENCES `Inventory` (`Item_number`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Order_Description`
--

LOCK TABLES `Order_Description` WRITE;
/*!40000 ALTER TABLE `Order_Description` DISABLE KEYS */;
INSERT INTO `Order_Description` VALUES (121,201,1000),(121,202,300),(122,203,700),(123,203,650),(124,202,500);
/*!40000 ALTER TABLE `Order_Description` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Orders`
--

DROP TABLE IF EXISTS `Orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Orders` (
  `Order_no` int NOT NULL,
  `Customer_name` varchar(50) DEFAULT NULL,
  `Order_date` date DEFAULT NULL,
  `Net_amount` int DEFAULT NULL,
  `Advance_paid` int DEFAULT NULL,
  `Order_status` varchar(50) DEFAULT NULL,
  `Shipping_date` date DEFAULT NULL,
  `Discount` int DEFAULT NULL,
  PRIMARY KEY (`Order_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Orders`
--

LOCK TABLES `Orders` WRITE;
/*!40000 ALTER TABLE `Orders` DISABLE KEYS */;
INSERT INTO `Orders` VALUES (121,'Himanshu','2022-01-25',20000,18000,'Dispatched','2022-01-08',5),(122,'Shivam','2022-01-15',50000,30000,'To be Shipped','2022-01-18',3),(123,'Arnav','2022-01-16',35000,30000,'Delivered','2022-01-19',8),(124,'Bharat','2022-01-24',40000,20000,'Dispatched','2022-01-07',5);
/*!40000 ALTER TABLE `Orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Owner`
--

DROP TABLE IF EXISTS `Owner`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Owner` (
  `Fname` varchar(20) DEFAULT NULL,
  `Lname` varchar(20) DEFAULT NULL,
  `Owner_id` int NOT NULL,
  `Equity_share` int DEFAULT NULL,
  PRIMARY KEY (`Owner_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Owner`
--

LOCK TABLES `Owner` WRITE;
/*!40000 ALTER TABLE `Owner` DISABLE KEYS */;
INSERT INTO `Owner` VALUES ('Kabir','Shamlani',1,1),('Nipun','Tulsian',2,50),('Vyom','Goyal',3,49);
/*!40000 ALTER TABLE `Owner` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Payment`
--

DROP TABLE IF EXISTS `Payment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Payment` (
  `Order_no` int NOT NULL,
  `Pay_Mode` varchar(50) DEFAULT NULL,
  `Cheque_no` bigint DEFAULT NULL,
  `Amount` int DEFAULT NULL,
  `Pay_date` date DEFAULT NULL,
  PRIMARY KEY (`Order_no`),
  CONSTRAINT `Payment_ibfk_1` FOREIGN KEY (`Order_no`) REFERENCES `Orders` (`Order_no`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Payment`
--

LOCK TABLES `Payment` WRITE;
/*!40000 ALTER TABLE `Payment` DISABLE KEYS */;
INSERT INTO `Payment` VALUES (121,'Cash',NULL,30000,'2022-01-01'),(122,'Cheque',1234567890,50000,'2022-01-06'),(123,'Cash',NULL,100000,'2022-03-13'),(124,'Cash',NULL,28000,'2022-01-21');
/*!40000 ALTER TABLE `Payment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Pending_payments`
--

DROP TABLE IF EXISTS `Pending_payments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Pending_payments` (
  `Distributor_id` int NOT NULL,
  `Pending_Order_id` int NOT NULL,
  PRIMARY KEY (`Distributor_id`,`Pending_Order_id`),
  KEY `Pending_Order_id` (`Pending_Order_id`),
  CONSTRAINT `Pending_payments_ibfk_1` FOREIGN KEY (`Distributor_id`) REFERENCES `Distributors` (`Distributor_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Pending_payments_ibfk_2` FOREIGN KEY (`Pending_Order_id`) REFERENCES `Orders` (`Order_no`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Pending_payments`
--

LOCK TABLES `Pending_payments` WRITE;
/*!40000 ALTER TABLE `Pending_payments` DISABLE KEYS */;
INSERT INTO `Pending_payments` VALUES (1001,121),(1002,122),(1003,124);
/*!40000 ALTER TABLE `Pending_payments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Works_for`
--

DROP TABLE IF EXISTS `Works_for`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Works_for` (
  `Owner_id` int NOT NULL,
  `Employee_id` int NOT NULL,
  `Department_id` int NOT NULL,
  PRIMARY KEY (`Owner_id`,`Employee_id`,`Department_id`),
  KEY `Employee_id` (`Employee_id`),
  KEY `Department_id` (`Department_id`),
  CONSTRAINT `Works_for_ibfk_1` FOREIGN KEY (`Owner_id`) REFERENCES `Owner` (`Owner_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Works_for_ibfk_2` FOREIGN KEY (`Employee_id`) REFERENCES `Employee` (`Employee_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Works_for_ibfk_3` FOREIGN KEY (`Department_id`) REFERENCES `Department` (`Dno`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Works_for`
--

LOCK TABLES `Works_for` WRITE;
/*!40000 ALTER TABLE `Works_for` DISABLE KEYS */;
INSERT INTO `Works_for` VALUES (2,101,1),(3,102,2),(1,103,3),(3,104,1),(1,105,2),(2,106,3),(3,107,1),(2,108,2),(1,109,3),(2,110,1);
/*!40000 ALTER TABLE `Works_for` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-27 18:49:27
