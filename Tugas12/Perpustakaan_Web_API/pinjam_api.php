<?php
require_once 'database.php';
require_once 'Pinjam.php';
$db = new MySQLDatabase();
$pinjam = new Pinjam($db);
$id=0;
$nomorbukti=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];
// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET[''])){
            $nomorbukti = $_GET[''];
        }
        if($id>0){    
            $result = $pinjam->get_by_id($id);
        }elseif($nomorbukti>0){
            $result = $pinjam->get_by_nomorbukti($nomorbukti);
        } else {
            $result = $pinjam->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new pinjam
        $pinjam->nomorbukti = $_POST['nomorbukti'];
        $pinjam->tglpinjam = $_POST['tglpinjam'];
        $pinjam->kodeanggota = $_POST['kodeanggota'];
        $pinjam->kodebuku1 = $_POST['kodebuku1'];
        $pinjam->kodebuku2 = $_POST['kodebuku2'];
        $pinjam->tglhrskembali = $_POST['tglhrskembali'];
        $pinjam->tgldikembalikan = $_POST['tgldikembalikan'];
        $pinjam->statuspinjam = $_POST['statuspinjam'];
        $pinjam->denda = $_POST['denda'];
       
        $pinjam->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Pinjam created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Pinjam not created.';
        }
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'PUT':
        // Update an existing data
        $_PUT = [];
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET[''])){
            $nomorbukti = $_GET[''];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $pinjam->nomorbukti = $_PUT['nomorbukti'];
        $pinjam->tglpinjam = $_PUT['tglpinjam'];
        $pinjam->kodeanggota = $_PUT['kodeanggota'];
        $pinjam->kodebuku1 = $_PUT['kodebuku1'];
        $pinjam->kodebuku2 = $_PUT['kodebuku2'];
        $pinjam->tglhrskembali = $_PUT['tglhrskembali'];
        $pinjam->tgldikembalikan = $_PUT['tgldikembalikan'];
        $pinjam->statuspinjam = $_PUT['statuspinjam'];
        $pinjam->denda = $_PUT['denda'];
        if($id>0){    
            $pinjam->update($id);
        }elseif($pinjam<>""){
            $pinjam->update_by_nomorbukti($nomorbukti);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Pinjam updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Pinjam update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET[''])){
            $nomorbukti = $_GET[''];
        }
        if($id>0){    
            $pinjam->delete($id);
        }elseif($nomorbukti>0){
            $pinjam->delete_by_nomorbukti($nomorbukti);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Pinjam deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Pinjam delete failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    default:
        header("HTTP/1.0 405 Method Not Allowed");
        break;
    }
$db->close()
?>