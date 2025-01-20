
## コンテスト開始時にやること
data.jsonのcontest_idを変更する
```json: data.json
{
    "contest_id": "abc100"
}
```
それだけ！

## テストの実行
```sh
./tools/test.py
```
を実行する。<br>
タスクを聞かれるので答える。aとかbとか



## `.archive`フォルダ
このフォルダには解いたあとのmain.rsを保存する。<br>
増えていったら達成感とかありそうだし、過去の実装を参考にできることもありそうだから。<br>
追加する際は以下のコマンドを実行する。
```sh
./tools/save.sh
```

