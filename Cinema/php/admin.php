<?php
// Formulário para adicionar novo filme
echo "<form method='POST' enctype='multipart/form-data'>";
echo "<input type='text' name='titulo' placeholder='Título'>";
echo "<textarea name='descricao' placeholder='Descrição'></textarea>";
echo "<input type='file' name='poster'>";
echo "<button type='submit'>Adicionar Filme</button>";
echo "</form>";
 
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
  $titulo = $_POST['titulo'];
  $descricao = $_POST['descricao'];
  $poster = $_FILES['poster']['name'];
  move_uploaded_file($_FILES['poster']['tmp_name'], 'images/'.$poster);
  $conn = new mysqli('localhost', 'root', '', 'cinema_db');
  $stmt = $conn->prepare("INSERT INTO filmes (titulo, descricao, poster) VALUES (?, ?, ?)");
  $stmt->bind_param('sss', $titulo, $descricao, $poster);
  $stmt->execute();
  echo "Filme adicionado!";
}
?>