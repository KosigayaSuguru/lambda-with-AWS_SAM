# lambda template with AWS SAM

## アプリケーションの配置について

top(hello_world)/階層名(aaa)/Function名（lambda1） とする。  
階層名を挟むのは、Function名ディレクトリに配置されたpythonコードの中で相対importを使用するため。  
階層名は一意になれば何でもいい。

相対importを使用するのは、補完を正常に働かせるため。
例えば↓のような構成をとったとして、

```text
lamnbda1
+- app.py, main.py
lamnbda2
+- app.py, main.py
```

下記の状態の場合、

* lambda1、lambda2をそれぞれpythonpathとして指定する
* app.py の中で main.py を import する

それぞれのapp.pyから見た場合、lambda1、lambda2の main.py は区別がつかないため、補完がおかしくなる。  
※SAMで起動される際には template.yaml で CodeUri を指定するので、アプリケーションとしては動く。（多分。。


## requirements.txt について

SAMの template.yaml 内で指定されている CodeUri に内に requirements.txt がないとSAMのbuild時に怒られる。  
※中身が空であっても存在自体が必要

Function個別に requirements.txt を配置すれば動作はするが、1つのリポジトリに対して、 requirements.txt という状況にしておきたいのが心情。  
このため、シンボリックリンクを使用して、 requirements.txt を共有する。

### シンボリックリンク作成手順

下記を実行する。（とりあえずwindowsから前提）

```bat
cd template.yamlのCodeUriのパス
mklink requirements.txt targetのrequirements.txt
```

※上記で作成したファイルがLinux上から読み込んでも機能していることは使って確認済み。（DockerでVolume使った。

### requirements.txt に記載されているライブラリの取り扱い

#### ローカル開発時

↓して普通にvenvにインストールする。
```bash
pip install -r requirements.txt
```

#### SAMによる実行、アップロード時

template.yaml の CodeUri と同場所に配置されているシンボリックリンクの requirements.txt を使用してbuildが行われる。
