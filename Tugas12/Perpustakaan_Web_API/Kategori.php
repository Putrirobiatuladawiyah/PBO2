<?php
//Simpanlah dengan nama file : Kategori.php
require_once 'database.php';
class Kategori 
{
    private $db;
    private $table = 'kategori';
    public $kodekategori = "";
    public $nama_kategori = "";
    public $judulbuku = "";
    public function __construct(MySQLDatabase $db)
    {
        $this->db = $db;
    }
    public function get_all() 
    {
        $query = "SELECT * FROM $this->table";
        $result_set = $this->db->query($query);
        return $result_set;
    }
    public function get_by_id(int $id)
    {
        $query = "SELECT * FROM $this->table WHERE id = $id";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function get_by_kodekategori(int $kodekategori)
    {
        $query = "SELECT * FROM $this->table WHERE kodekategori = $kodekategori";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`kodekategori`,`nama_kategori`,`judulbuku`) VALUES ('$this->kodekategori','$this->nama_kategori','$this->judulbuku')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET kodekategori = '$this->kodekategori', nama_kategori = '$this->nama_kategori', judulbuku = '$this->judulbuku' 
        WHERE idkategori = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_kodekategori($kodekategori): int
    {
        $query = "UPDATE $this->table SET kodekategori = '$this->kodekategori', nama_kategori = '$this->nama_kategori', judulbuku = '$this->judulbuku' 
        WHERE kodekategori = $kodekategori";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE idkategori = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_kodekategori($kodekategori): int
    {
        $query = "DELETE FROM $this->table WHERE kodekategori = $kodekategori";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>