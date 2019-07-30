:リモートリポジトリのクローンを作成する。
cd c:\djangos\django_dev\mobpj
git clone https://github.com/R-D-project/R_repo01.git .
git branch
git branch -r
git checkout -b mobbranch origin/mobbranch
git branch
git remote set-url origin https://R-D-project:rdpassword01@github.com/R-D-project/R_repo01.git
git config --local -l