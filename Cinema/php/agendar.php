<?php
  if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $nome_cliente = $_POST['nome'];
    $sessao_id = $_POST['sessao'];
    $quantidade = $_POST['quantidade'];
 
    $conn = new mysqli('localhost', 'root', '', 'cinema_db');
    $stmt = $conn->prepare("INSERT INTO reservas (sessao_id, nome_cliente, quantidade) VALUES (?, ?, ?)");
    $stmt->bind_param('isi', $sessao_id, $nome_cliente, $quantidade);
    $stmt->execute();
    echo "Reserva feita com sucesso!";
  }
 
  // Exibir formulário de reserva
  echo "<form method='POST'>";
  echo "<input type='text' name='nome' placeholder='Seu nome'>";
  echo "<select name='sessao'>";
  $result = $conn->query("SELECT * FROM sessoes");
  while ($sessao = $result->fetch_assoc()) {
    echo "<option value='".$sessao['id']."'>Sessão: ".$sessao['data']." às ".$sessao['horario']."</option>";
  }
  echo "</select>";
  echo "<input type='number' name='quantidade' placeholder='Ingressos'>";
  echo "<button type='submit'>Agendar</button>";
  echo "</form>";
?>