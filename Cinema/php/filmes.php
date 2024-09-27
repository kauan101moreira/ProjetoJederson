<?php
  $filme_id = $_GET['id'];
  $conn = new mysqli('localhost', 'root', '', 'cinema_db');
  $result = $conn->query("SELECT * FROM filmes WHERE id=$filme_id");
 
  if ($filme = $result->fetch_assoc()) {
    echo "<h1>".$filme['titulo']."</h1>";
    echo "<p>".$filme['descricao']."</p>";
    echo "<p>Gênero: ".$filme['genero']."</p>";
    echo "<p>Classificação: ".$filme['classificacao']."</p>";
    echo "<p>Duração: ".$filme['duracao']." minutos</p>";
  }
 
  // Exibir sessões disponíveis
  $sessoes = $conn->query("SELECT * FROM sessoes WHERE filme_id=$filme_id");
  while ($sessao = $sessoes->fetch_assoc()) {
    echo "<p>Sessão: ".$sessao['data']." às ".$sessao['horario']." - Sala ".$sessao['sala']."</p>";
  }
?>