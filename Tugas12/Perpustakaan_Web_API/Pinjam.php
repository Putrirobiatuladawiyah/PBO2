<?php
//Simpanlah dengan nama file : Pinjam.php
require_once 'database.php';
class Pinjam 
{
    private $db;
    private $table = 'pinjam';
    public $nomorbukti = "";
    public $tglpinjam = "";
    public $kodeanggota = "";
    public $kodebuku1 = "";
    public $kodebuku2 = "";
    public $tglhrskembali = "";
    public $tgldikembalikan = "";
    public $statuspinjam = "";
    public $denda = "";
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
    public function get_by_nomorbukti(string $nomorbukti) 
    {
        $query = "SELECT * FROM $this->table WHERE  nomorbukti = '$nomorbukti'"; // Menambahkan tanda kutip pada nilai $nomorbukti
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`nomorbukti`,`tglpinjam`,`kodeanggota`,`kodebuku1`,`kodebuku2`,`tglhrskembali`,`tgldikembalikan`,`statuspinjam`,`denda`) VALUES ('$this->nomorbukti','$this->tglpinjam','$this->kodeanggota','$this->kodebuku1','$this->kodebuku2','$this->tglhrskembali','$this->tgldikembalikan','$this->statuspinjam','$this->denda')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET nomorbukti = '$this->nomorbukti', tglpinjam = '$this->tglpinjam', kodeanggota = '$this->kodeanggota', kodebuku1 = '$this->kodebuku1', kodebuku2 = '$this->kodebuku2', tglhrskembali = '$this->tglhrskembali', tgldikembalikan = '$this->tgldikembalikan', statuspinjam = '$this->statuspinjam', denda = '$this->denda' 
        WHERE idpinjam = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_nomorbukti(string $nomorbukti): int
    {
        $query = "UPDATE $this->table SET nomorbukti = '$nomorbukti', tglpinjam = '$this->tglpinjam', kodeanggota = '$this->kodeanggota', kodebuku1 = '$this->kodebuku1', kodebuku2 = '$this->kodebuku2', tglhrskembali = '$this->tglhrskembali', tgldikembalikan = '$this->tgldikembalikan', statuspinjam = '$this->statuspinjam', denda = '$this->denda' 
        WHERE nomorbukti = '$nomorbukti'"; // Ganti <nama_kolom> dan <nilai_kolom> sesuai dengan nama kolom dan nilai yang sesuai. 
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE idpinjam = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_nomorbukti(string $nomorbukti): int
    {
        $query = "DELETE FROM $this->table WHERE nomorbukti = $nomorbukti";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>