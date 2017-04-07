<html>

<?php 
// define variables and set to empty values
$name = $email = $gender = $comment = $website = "";
echo "done."

if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $name = test_input($_POST["first_name"]);
  $email = test_input($_POST["last_name"]);
  $website = test_input($_POST["user_id"]);
  $comment = test_input($_POST["password"]);
  $gender = test_input($_POST["gender"]);
  echo $name
  echo $email
  echo $website
  echo $comment
  echo $gender
}

function test_input($data) {
  $data = trim($data);
  $data = stripslashes($data);
  $data = htmlspecialchars($data);
  return $data;
}
?>
</html>