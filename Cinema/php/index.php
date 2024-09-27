<?php
  $conn = new mysqli('localhost', 'root', '', 'cinema_db');
  $result = $conn->query("SELECT * FROM filmes");
 
  while ($filme = $result->fetch_assoc()) {
    echo "<div class='filme'>";
    echo "<img src='images/".$filme['poster']."' alt='".$filme['titulo']."'>";
    echo "<h2>".$filme['titulo']."</h2>";
    echo "<p>".$filme['descricao']."</p>";
    echo "</div>";
  }
?>