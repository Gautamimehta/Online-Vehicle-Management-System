<?php

$name=filter_input(INPUT-POST,'name');

$email=filter_input(INPUT-POST,'email');
if(!empty($name)){
if(!empty($password)){
$host="localhost";
$dbusername="";
$dbpassword="2000";
$dbname="my";
$conn=new mysqli($host,$dbusername,$dbpassword,$dbname);
if(mysqli_connect_error()){
die('Connect Error('.mysqli_connect_errno().')'
.mysqli_connect_error());
}
else{
$sql="INSERT INTO enter(name,email) values('$name','email')";
if($conn->query($sql)){
echo " New record imserted";
}
else{
echo" error";
}
$conn->close(); 
}
}
else{
echo "Password should not be empty";
die();
}
}
else{
echo "username shoul not be empty";
die();
}
?>