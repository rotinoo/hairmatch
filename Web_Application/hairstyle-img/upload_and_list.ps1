# ---------------------------------------------------------------
# Script: upload_and_list.ps1
# Deskripsi: Mengupload gambar ke GCS dan mencatat metadata ke CSV.
# ---------------------------------------------------------------

# -------------------------
# 1. Konfigurasi Variabel
# -------------------------
$BUCKET_NAME = "hairmatch-hairstyle-img"  # Nama bucket GCS Anda
$CSV_FILE = "image_list.csv"              # Nama file CSV output
$BASE_DIR = "C:\Project\hairmatch\Web_Application\hairstyle-img"  # Direktori dasar gambar

# -------------------------------
# 2. Inisialisasi File CSV
# -------------------------------
# Hapus atau buat ulang file CSV untuk memastikan kosong
if (Test-Path -Path $CSV_FILE) {
    Remove-Item -Path $CSV_FILE -Force
}
New-Item -Path $CSV_FILE -ItemType File -Force | Out-Null

# Tambahkan header ke CSV
"Category,File Name,File URL" | Out-File -FilePath $CSV_FILE -Encoding UTF8

# -------------------------------
# 3. Fungsi untuk Mengupload dan Mencatat
# -------------------------------
function Upload-And-LogImage {
    param (
        [string]$ImagePath,
        [string]$CategoryName
    )

    $FileName = [System.IO.Path]::GetFileName($ImagePath)
    Write-Output "Uploading: $FileName"

    # Upload file ke GCS
    gsutil cp "`"$ImagePath`"" "gs://$BUCKET_NAME/$CategoryName/"

    # Cek apakah upload berhasil
    if ($LASTEXITCODE -eq 0) {
        # Generate URL publik
        $FileURL = "https://storage.googleapis.com/$BUCKET_NAME/$CategoryName/$FileName"

        # Tambahkan entri ke CSV dengan mengelilingi setiap field dengan tanda kutip ganda
        "`"$CategoryName`",`"$FileName`",`"$FileURL`"" | Out-File -FilePath $CSV_FILE -Encoding UTF8 -Append
        Write-Output "Uploaded and logged: $FileName"
    }
    else {
        Write-Warning "Failed to upload $FileName"
    }
}

# -------------------------------
# 4. Loop Melalui Kategori dan Gambar
# -------------------------------
# Dapatkan semua direktori (kategori) dalam BASE_DIR
$Categories = Get-ChildItem -Path $BASE_DIR -Directory

foreach ($Category in $Categories) {
    $CategoryName = $Category.Name
    Write-Output "Processing category: $CategoryName"

    # Dapatkan semua file gambar dalam kategori
    $ImageFiles = Get-ChildItem -Path $Category.FullName -File | Where-Object { $_.Extension -match "\.(jpg|jpeg|png)$" }

    foreach ($Image in $ImageFiles) {
        Upload-And-LogImage -ImagePath $Image.FullName -CategoryName $CategoryName
    }
}

# -------------------------------
# 5. Penyelesaian
# -------------------------------
Write-Output "Upload complete. CSV generated at $CSV_FILE."
