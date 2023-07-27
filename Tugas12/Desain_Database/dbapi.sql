-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 18, 2023 at 01:51 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 7.4.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dbapi`
--

-- --------------------------------------------------------

--
-- Table structure for table `anggota`
--

CREATE TABLE `anggota` (
  `idanggota` int(11) NOT NULL,
  `kodeanggota` varchar(20) NOT NULL,
  `nama` varchar(100) NOT NULL,
  `jk` char(1) NOT NULL,
  `alamat` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `anggota`
--

INSERT INTO `anggota` (`idanggota`, `kodeanggota`, `nama`, `jk`, `alamat`) VALUES
(1, '210511034', 'Aghisna Baihaqi', 'P', 'Subang'),
(2, '210511018', 'Putri Robiatul Adawiyah', 'P', 'Brebes'),
(3, '210511025', 'Rifa Nurfaizah', 'P', 'Cirebon'),
(4, '210511012', 'Hanafiyatussamhah', 'P', 'Garut');

-- --------------------------------------------------------

--
-- Table structure for table `buku`
--

CREATE TABLE `buku` (
  `idbuku` int(11) NOT NULL,
  `kodebuku` varchar(11) NOT NULL,
  `judul` varchar(22) NOT NULL,
  `pengarang` varchar(100) NOT NULL,
  `penerbit` varchar(100) NOT NULL,
  `tahun` varchar(4) NOT NULL,
  `kodekategori` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `buku`
--

INSERT INTO `buku` (`idbuku`, `kodebuku`, `judul`, `pengarang`, `penerbit`, `tahun`, `kodekategori`) VALUES
(1, '1000', 'Aplikasi Komputer', 'Dedy Iswanto', 'Mitra Wacana Media', '2018', 0),
(3, '1001', 'Modul Struktur Data', 'Kelompok 4-TIF-R1-UMC', 'UMC', '2023', 2),
(4, '1002', 'Modul Struktur Data', 'Kelompok 5-TIF-R1-UMC', 'UMC', '2023', 3),
(5, '1003', 'Laskar Pelangi', 'Andrea Hirata', 'Bentang Pustaka', '2005', 4);

-- --------------------------------------------------------

--
-- Table structure for table `dosen`
--

CREATE TABLE `dosen` (
  `nid` int(11) NOT NULL,
  `nidn` int(11) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `jk` char(1) NOT NULL,
  `prodi` varchar(20) NOT NULL,
  `jabatan` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `dosen`
--

INSERT INTO `dosen` (`nid`, `nidn`, `nama`, `jk`, `prodi`, `jabatan`) VALUES
(1, 6001, 'Ahmad', 'L', 'PET', 'Kaprodi'),
(2, 6002, 'Freddy W.M.Kom', 'L', '08976543234', 'DT'),
(4, 6004, 'Harry Gunawan, M.kom', 'L', '0876897654', 'DT'),
(7, 5678, 'Haris', 'L', '08964553', 'DLB'),
(9, 6007, 'Arie Susetyo', 'P', 'IND', 'Kaprodi'),
(12, 6008, 'Dian Novianti, M.Kom', 'P', 'TIF', 'Kaprodi'),
(14, 6018, 'Putri', 'P', 'TIF', 'Kaprodi'),
(19, 1234, 'Hyunjin', 'L', 'IND', 'Kaprodi'),
(20, 1222, 'Putt', 'P', 'TIF', 'DT');

-- --------------------------------------------------------

--
-- Table structure for table `kategori`
--

CREATE TABLE `kategori` (
  `idkategori` int(11) NOT NULL,
  `kodekategori` int(20) NOT NULL,
  `nama_kategori` varchar(100) NOT NULL,
  `judulbuku` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `kategori`
--

INSERT INTO `kategori` (`idkategori`, `kodekategori`, `nama_kategori`, `judulbuku`) VALUES
(1, 123, 'Buku Informatika', 'Aplikasi Komputer'),
(2, 224, 'Buku teknik Industri', 'Pengantar Teknik Industri'),
(3, 167, 'Buku Peternakan', 'Agribisnis Pembibitan Ternak'),
(23, 555, 'Buku AIK', 'Aqidah Ibadah');

-- --------------------------------------------------------

--
-- Table structure for table `mahasiswa`
--

CREATE TABLE `mahasiswa` (
  `id` int(11) NOT NULL,
  `nim` varchar(10) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `jk` enum('L','P') NOT NULL DEFAULT 'L',
  `prodi` enum('IND','TIF','PET') NOT NULL DEFAULT 'TIF'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `mahasiswa`
--

INSERT INTO `mahasiswa` (`id`, `nim`, `nama`, `jk`, `prodi`) VALUES
(2, '1002', 'Hanafia', 'P', 'TIF'),
(4, '1003', 'Risna Yulianti', 'P', 'IND'),
(12, '5567', 'Rahma', 'P', 'IND'),
(13, '6678', 'Haris', 'P', 'IND'),
(15, '1011', 'Budi Susanto', 'L', 'IND'),
(22, '210511018', 'Putri Robiatul Adawiyah', 'P', 'TIF'),
(23, '1004', 'Rose', 'P', 'TIF'),
(24, '1005', 'Hyunjin', 'L', 'PET');

-- --------------------------------------------------------

--
-- Table structure for table `matakuliah`
--

CREATE TABLE `matakuliah` (
  `idmk` int(11) NOT NULL,
  `kodemk` varchar(10) NOT NULL,
  `namamk` varchar(100) NOT NULL,
  `sks` int(11) NOT NULL,
  `prodi` char(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `matakuliah`
--

INSERT INTO `matakuliah` (`idmk`, `kodemk`, `namamk`, `sks`, `prodi`) VALUES
(1, '2010', 'Pemrograman Visual', 3, 'TIF'),
(2, '2011', 'Pemrograman Bergerak', 3, 'D3TIF'),
(3, '2022', 'KALKULUS II', 3, 'IND'),
(6, '2222', 'AIK', 3, 'TIF');

-- --------------------------------------------------------

--
-- Table structure for table `pinjam`
--

CREATE TABLE `pinjam` (
  `idpinjam` int(11) NOT NULL,
  `nomorbukti` varchar(20) NOT NULL,
  `tglpinjam` date NOT NULL,
  `kodeanggota` varchar(20) NOT NULL,
  `kodebuku1` varchar(20) NOT NULL,
  `kodebuku2` varchar(20) NOT NULL,
  `tglhrskembali` date NOT NULL,
  `tgldikembalikan` date NOT NULL,
  `statuspinjam` varchar(100) NOT NULL,
  `denda` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `pinjam`
--

INSERT INTO `pinjam` (`idpinjam`, `nomorbukti`, `tglpinjam`, `kodeanggota`, `kodebuku1`, `kodebuku2`, `tglhrskembali`, `tgldikembalikan`, `statuspinjam`, `denda`) VALUES
(1, '123', '2023-01-18', '210511034', 'ATIF0001', 'BTIF0001', '2023-01-26', '2023-01-26', 'Sudah Dikembalikan', '-'),
(2, '223', '2023-01-19', '210511018', 'ATIF0002', 'ATIF0001', '2023-01-25', '2023-02-02', 'Sudah Dikembalikan', '10.000'),
(3, '555', '2023-06-17', '210611019', 'ATIF0002', 'BTIF0002', '2023-06-22', '2023-06-21', 'Sudah dikembalikan', '-'),
(4, '666', '2023-06-17', '210611019', 'ATIF0002', 'BTIF0002', '2023-06-22', '2023-06-21', 'Sudah dikembalikan', '-'),
(10, '190', '2023-06-17', '210611019', 'ATIF0002', 'BTIF0002', '2023-06-22', '2023-06-21', 'Sudah dikembalikan', '-'),
(11, '224', '2023-06-18', '2147483647', 'APT0001', 'BPT0001', '2023-06-20', '2023-06-22', 'TELATT', '10000'),
(12, '', '2023-06-17', '210611019', 'ATIF0002', 'BTIF0002', '2023-06-22', '2023-06-21', 'Sudah dikembalikan', '-'),
(13, '', '2023-06-17', '210611019', 'ATIF0002', 'BTIF0002', '2023-06-22', '2023-06-21', 'Sudah dikembalikan', '-'),
(14, '', '2023-06-17', '210611019', 'ATIF0002', 'BTIF0002', '2023-06-22', '2023-06-21', 'Sudah dikembalikan', '-');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `passwd` varchar(50) NOT NULL,
  `rolename` enum('admin','petugas','mahasiswa') NOT NULL DEFAULT 'mahasiswa'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `passwd`, `rolename`) VALUES
(1, 'tatang', '202cb962ac59075b964b07152d234b70', 'admin'),
(2, 'putri', '4093fed663717c843bea100d17fb67c8', 'petugas'),
(3, 'farhan', '202cb962ac59075b964b07152d234b70', 'mahasiswa');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `anggota`
--
ALTER TABLE `anggota`
  ADD PRIMARY KEY (`idanggota`),
  ADD UNIQUE KEY `kodeanggota` (`kodeanggota`);

--
-- Indexes for table `buku`
--
ALTER TABLE `buku`
  ADD PRIMARY KEY (`idbuku`),
  ADD UNIQUE KEY `kodebuku` (`kodebuku`);

--
-- Indexes for table `dosen`
--
ALTER TABLE `dosen`
  ADD PRIMARY KEY (`nid`),
  ADD UNIQUE KEY `unik` (`nidn`);

--
-- Indexes for table `kategori`
--
ALTER TABLE `kategori`
  ADD PRIMARY KEY (`idkategori`),
  ADD UNIQUE KEY `kodekategori` (`kodekategori`) USING BTREE;

--
-- Indexes for table `mahasiswa`
--
ALTER TABLE `mahasiswa`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nim` (`nim`);

--
-- Indexes for table `matakuliah`
--
ALTER TABLE `matakuliah`
  ADD PRIMARY KEY (`idmk`),
  ADD UNIQUE KEY `unik` (`kodemk`);

--
-- Indexes for table `pinjam`
--
ALTER TABLE `pinjam`
  ADD PRIMARY KEY (`idpinjam`),
  ADD KEY `nomorbukti` (`nomorbukti`) USING BTREE;

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `idx` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `anggota`
--
ALTER TABLE `anggota`
  MODIFY `idanggota` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `buku`
--
ALTER TABLE `buku`
  MODIFY `idbuku` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `dosen`
--
ALTER TABLE `dosen`
  MODIFY `nid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `kategori`
--
ALTER TABLE `kategori`
  MODIFY `idkategori` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `mahasiswa`
--
ALTER TABLE `mahasiswa`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `matakuliah`
--
ALTER TABLE `matakuliah`
  MODIFY `idmk` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `pinjam`
--
ALTER TABLE `pinjam`
  MODIFY `idpinjam` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
