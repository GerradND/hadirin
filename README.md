# Hadirin

[![pipeline status][pipeline-badge]][commits-gl]
[![coverage report][coverage-badge]][commits-gl]

Repo ini menyimpan TK Kelompok 10 mata kuliah RPL Ganjil 2021/2022

## Instruksi penggunaan

1. Buat direktori untuk proyek yang akan kamu buat (contoh: `project_name`), lalu
   buka Command Prompt (cmd) atau Terminal di dalam direktori tersebut.

2. Buat Python *virtual environment* di dalamnya.

   ```shell
   python -m venv venv
   ```

   > Catatan: sesuaikan dengan *executable* `python` yang ada di komputer kamu,
   > karena terkadang (misal: di Ubuntu atau macOS) Python 3 hanya bisa
   > dipanggil dengan `python3`, bukan `python`.

3. Aktifkan *virtual environment* yang telah dibuat.\
   Di Windows:

   ```shell
   venv\Scripts\activate
   ```

   Di Linux/macOS:

   ```shell
   source venv/bin/activate
   ```

   Jika berhasil, akan muncul `(venv)` pada *prompt* cmd/terminal kamu.

4.  Instal terlebih dahulu *package-package* yang
    diperlukan dengan perintah berikut.

    ```shell
    python -m pip install -r requirements.txt
    ```

14. Lanjutkan dengan membuat basis data lokal dan mengumpulkan
    berkas *static* menjadi satu direktori dengan perintah-perintah berikut.

    ```shell
    python manage.py migrate
    python manage.py collectstatic
    ```
15. Jika sudah, kamu bisa menjalankan *web server* kamu secara lokal dengan
    perintah berikut.

    ```shell
    python manage.py runserver
    ```

16. Mulai dari sini, kamu cukup edit berkas-berkas proyek Django kamu
    sesuai kebutuhan. Lalu, jangan lupa gunakan perintah `git add`,
    `git commit`, dan `git push` untuk mengunggah perubahanmu ke GitLab/GitHub
    (yang kemudian akan di-*deploy* ke Heroku). Jangan lupa untuk membuat
    berkas-berkas *migrations* jika kamu mengubah berkas `models.py`.

    ```shell
    python manage.py makemigrations
    ```

    Berkas-berkas *migrations* yang dihasilkan **harus** dimasukkan ke dalam
    repositori <sup><sub>(kecuali kamu mengubah konfigurasi templat sehingga
    hal tersebut tidak diperlukan... tetapi mengapa?)</sub></sup>.

17. Untuk menjalankan *unit test*, kamu bisa gunakan perintah berikut.

    ```shell
    python manage.py test --exclude-tag=functional
    ```

[pipeline-badge]: https://gitlab.com/tk-rpl-a/hadirin/badges/main/pipeline.svg
[coverage-badge]: https://gitlab.com/tk-rpl-a/hadirin/badges/main/coverage.svg
[commits-gl]: https://gitlab.com/tk-rpl-a/hadirin/-/commits/main
