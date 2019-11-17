# discordpy-startup
# -*- coding: utf-8 -*-

import sys
import discord
import random
import asyncio
import time
import datetime
import urllib.request
import json
import re
import os
import traceback


from discord.ext import tasks

TOKEN = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID = 623154510662991883
client = discord.Client()
dateTime = datetime.datetime.now()
server_number = len(client.guilds)
client.global_list = [] #グローバルチャット参加チャンネルのリスト
atk_ch_id = "#掃き溜め"
atk_ch = client.get_channel(643461030692782081)
q_ch = client.get_channel(644199380764721152)
help_ch = 642578258743001088
ModeFlag = 0



citycodes = {
    "北海道": '016010',"青森県": '020010',
    "岩手県": '030010',"宮城県": '040010',
    "秋田県": '050010',"山形県": '060010',
    "福島県": '070010',"東京都": '130010',
    "神奈川県": '140010',"埼玉県": '110010',
    "千葉県": '120010',"茨城県": '080010',
    "栃木県": '090010',"群馬県": '100010',
    "山梨県": '190010',"新潟県": '150010',
    "長野県": '200010',"富山県": '160010',
    "石川県": '170010',"福井県": '180010',
    "愛知県": '230010',"岐阜県": '200010',
    "静岡県": '220010',"三重県": '240010',
    "大阪府": '270000',"兵庫県": '280010',
    "京都府": '260010',"滋賀県": '250010',
    "奈良県": '190010',"和歌山県": '300010',
    "鳥取県": '310010',"島根県": '320010',
    "岡山県": '330010',"広島県": '340010',
    "山口県": '350010',"徳島県": '360010',
    "香川県": '370000',"愛媛県": '380010',
    "高知県": '390010',"福岡県": '400010',
    "大分県": '440010',"長崎県": '420010',
    "佐賀県": '410010',"熊本県": '430010',
    "宮崎県": '450010',"鹿児島県": '460010',
    "沖縄県": '471010',"北海": '016010',
    "青森": '020010',"岩手": '030010',
    "宮城": '040010',"秋田": '050010',
    "山形": '060010',"福島": '070010',
    "東京": '130010',"神奈川": '140010',
    "埼玉": '110010',"千葉": '120010',
    "茨城": '080010',"栃木": '090010',
    "群馬": '100010',"山梨": '190010',
    "新潟": '150010',"長野": '200010',
    "富山": '160010',"石川": '170010',
    "福井": '180010',"愛知": '230010',
    "岐阜": '200010',"静岡": '220010',
    "三重": '240010',"大阪": '270000',
    "兵庫": '280010',"京都": '260010',
    "滋賀": '250010',"奈良": '190010',
    "和歌山": '300010',"鳥取": '310010',
    "島根": '320010',"岡山": '330010',
    "広島": '340010',"山口": '350010',
    "徳島": '360010',"香川": '370000',
    "愛媛": '380010',"高知": '390010',
    "福岡": '400010',"大分": '440010',
    "長崎": '420010',"佐賀": '410010',
    "熊本": '430010',"宮崎": '450010',
    "鹿児島": '460010',"沖縄": '471010',
}

help_embed_0 = discord.Embed(title="⚠️YUI注意事項一覧⚠️",description = '🔷**[]は不要です**\n```y![example]→y!example```\n🔷**スペースの有無を確認して下さい**\n```y!example []→有り\ny!example[]→無し```\n🔷**管理者権限必須です**```YUIのコマンドにはYUIに管理者を持たせないと正常に作動しないものが多々御座います。ご注意ください```\n🔷**ニックネーム変更非推奨**```第２項TAO系コマンドは、YUIのニックネームが変わるとオートアタックのみ正常に動作しません。\nTAOに関連性を持たせないつもりであれば、ニックネームの変更は構いません```',color=discord.Colour.green())


help_embed = discord.Embed(title="TAOコマンド系ヘルプ━第２項",description="TAOで使うコマンドを使うヘルプだよ",color=discord.Colour.green())
#help_embed.add_field(name="```y!ch [channel ID]```",value='このコマンドを使った後に**ゆいがんばれ**って言ってくれたら指定したチャンネルでアタックをするから\n後でスイーツおごってもらうからね\n止めてほしいときは**ゆいおつかれ**って言って')
help_embed.add_field(
name='y!atkch [チャンネルメンション]'
,value='`指定した場所を対象に設定\n指定の場所でy!atk`'
,inline=True)

help_embed.add_field(
name='y!login'
,value='`ログインする`'
,inline=True)
help_embed.add_field(
name='y!st'
,value='`::st\n　　　　　`'
,inline=True)
help_embed.add_field(
name='y!i'
,value='`::item\n　　　　　`'
,inline=True)
help_embed.add_field(
name='y!i [f,e]'
,value='`::i [f,e]\n　　　　　`'
,inline=True)
help_embed.add_field(
name='y!re',value='`::ren\n　　　　　`'
,inline=True)
help_embed.add_field(
name='y!atk',value='`::atk\n　　　　　`'
,inline=True)
help_embed.add_field(
name='y!nekoshima',value='`超激レア枠が出るまでTAOさなきゃいけない\nモンスターの数を占う`'
,inline=False)


help_two_embed = discord.Embed(title="ゆいの機能ヘルプ━第３項"
        ,description="その多機能"
        ,color=discord.Colour.green())
#サーバーの情報を開示するよ\nコード基礎提供者:_toni
help_two_embed.add_field(name='y!dice [下限] [上限]'
        ,value ='```下限~上限の数の間でサイコロをふる```'
        ,inline=False)
help_two_embed.add_field(name='y!sinfo'
        ,value ='```サーバーの情報を開示```'
        ,inline=False)
help_two_embed.add_field(name='y!kuji'
        ,value ='```おみくじ```'
        ,inline=False)
help_two_embed.add_field(name='y!myicon'
        ,value ='```コマンド使用者のアイコン表示```'
        ,inline=False)
help_two_embed.add_field(name='y!poll [タイトル] [内容] '
        ,value ='```👍👎リアクションつきembedメッセージ送信```'
        ,inline=False)
help_two_embed.add_field(name='y!say',value ='```y!say1 [内容]│オウム返し\ny!say2 [題名] [内容]│embed形式送信\ny!say3 [題名] [内容]│embed+送信者メンション+時刻```',inline=False)
help_two_embed.add_field(name='y!clean [数]'
        ,value ='```鯖管理者権限持ちで使用可、指定数のメッセージ消去```'
        ,inline=False)
help_two_embed.add_field(name='y!report [内容]'
        ,value ='```開発者へのレポート＆リクエスト```'
        ,inline=False)
help_two_embed.add_field(name='y!wt [都道府県名]',value='```今日、明日の天気予報「YUI WEATHER」```',inline=True)

embed_special = discord.Embed(
    title='特殊チャンネル系━第４項',
    description='```‣チャンネル内容│チャンネル名\nチャンネル作成コマンド```',color=discord.Colour.green())
embed_special.add_field(name='‣グローバルチャット│global_yui'
        ,value='```y!yui global```',inline=True)
embed_special.add_field(name='‣YUIの起動ログ│yui起動ログ'
        ,value ='```y!yui log```'
        ,inline=True)
embed_special.add_field(name='‣日付変更ログ│yui時報ログ'
        ,value ='```y!yui timelog```')


gacha = discord.Embed(title="ガチャ機能だよ🎯 ━第５頁"
,description="コマンドはy!gacha [ガチャ番号]"
,color=discord.Colour.green()
,inline=False)
gacha.set_thumbnail(url="https://yahoo.jp/box/HYqbOS")
gacha.add_field(name="ガチャ種類＋番号一覧",value="‣__**通常ガチャ**　番号：1__\n色々よくわからないものが出てくるよ。\nたまに隠しコマンドが出てくるとかなんとか\ny!gacha 1\n\n‣__**おにゃのこガチャ**　番号：2__\n可愛いおにゃのこの画像がいっぱいだよ\n可愛いの純度１００％！\ny!gacha 2")

slot_embed = discord.Embed(title="スロット機能だよ🎰━第６頁",description="コマンドはy!slot [s,c]",color=discord.Colour.green())
slot_embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/635993816297504809/642579874816720916/money_slot_machine.png")
slot_embed.add_field(name="スロット説明",value="絵文字を利用したスロットだよ\n表示が崩れるから、スマホとパソコンPCでコマンドを分けてるよ\n`y!slot s`がスマホ\n`y!slot c`がPCだよ\nちなみに開発者のスマホ（泥）を基準にしてるからIOS勢は表記が崩れるかも！\n泥勢もテキストサイズ変えちゃったら崩れるからね")

url_embed = discord.Embed(title='YUI関連URL━第７頁')
url_embed.add_field(name ='‣招待URL' ,value ='[ここをクリック🔘](https://discordapp.com/api/oauth2/authorize?client_id=627052576810074112&permissions=0&scope=bot)')
url_embed.add_field(name ='‣YUIサポートサーバー(仮)',value ='[ここをクリック🔘](https://discord.gg/SHxgnu)')


@client.event
async def on_ready():

    client.ch = client.get_channel(644199380764721152)
    client.already_quiz = {'漢字で「山葵(やま・あおい)」と書く香辛料はどれ?': 'わさび', 
'歌集「みだれ髪」の作者は誰?': '与謝野晶子', 
'小説「宝島」で、海賊ジョン・シルバーの肩にいつもとまっている鳥はどれ?': 'オウム', 
'野球のスコアで三振を表すアルファベット１文字はＫですが四球を表すアルファベット１文字は何？': 'Ｂ', 
'大ヒット映画「踊る大捜査線 THE MOVIE2」で、主役の刑事の名前はどれ?': '青島俊作', 
'1185年に源頼朝が設置したのは、守護とどれ?': '地頭', 
'女性ユニットYeLLOW Generationのプロデュースを手がける構成作家は誰？': 'おちまさと', 
'「米沢牛」で知られる米沢市がある件はどこ?': '山形県', 
'頭髪が蛇で出来ているギリシア神話の怪物はどれ?': 'メドゥーサ', 
'「政府開発援助」を表す言葉はどれ?': 'ODA', 
'「ナマズ」を英語で何という?': 'キャットフィッシュ', 
'JRの「学生割引」は、大人運賃の何割引き?': '2割', 
'西武ライオンズ前監督・東尾修の長女、東尾理子は何のプロ選手?': 'ゴルフ', 
'クリント・イーストウッドの吹き替えやルパン三世役で知られる声優は山田康雄ですがその山田の死後ルパン三世役を引き継いだモノマネ芸人といえば？': '栗田貫一', 
'次のうち、石川県で生産される焼き物はどれ?': '九谷焼', 
'スーパーマンの主人公、クラーク・ケントの普段の職業はどれ?': '新聞記者', 
'三島由紀夫の小説「金閣寺」で、金閣寺に放火した僧の名前はどれ?': '溝口', 
'1877年の西南戦争で反乱軍の指導者は誰?': '西郷隆盛', 
'第１回ラグビーＷ杯の優勝国はニュージーランドですが第２回ラグビーＷ杯の優勝国はどこ？': 'オーストラリア', 
'15世紀後半に、足利義政によって建てられた寺はどれ?': '銀閣寺', 
'昔話桃太郎で、桃太郎がイヌ・サル・キジを家来にするときに与えた食べ物は？': 'きび団子', 
'2005年にＴＢＳの女子アナウンサー小倉弘子と結婚した元Ｊリーガーは？': '水内猛', '童話「ピノキオ」で、ピノキオが嘘をつくと伸びる体の部分はどこ?': '鼻', 
'1991年に女子サッカーの第１回世界選手権が開催された国は中国ですがその大会で初代王者に輝いた国はどこ？': 'アメリカ', 
'映画風と共に去りぬでスカーレット・オハラを演じた女優はビビアン・リーですがレット・バトラーを演じた俳優は？': 'クラーク・ゲーブル', 
'デュエット曲「いつでも夢を」を歌ったのは、橋幸夫と誰?': '吉永小百合', 
'ピアノ曲集子供の領分で知られる作曲家はドビュッシーですがピアノ組曲子供の遊びで知られる作曲家は？': 'ビゼー', 
'次のうち正しい歩行者専用の交通標識はどれ？': '大人1人+子供1人', 
'次のうち、屋根が開閉式のドーム球場はどれ?': '福岡ドーム', 
'漫画めぞん一刻で三鷹が犬恐怖症を克服するために飼った犬の名前は？': 'マッケンロー', 
'「ちゃんぷるー」「らふてー」といえば、どこの料理?': '沖縄県', 
'革製品に使われるカーフスキンは子ウシの革ですがゴートスキンは何の革？': 'ヤギ', 
'映画「アルマゲドン」「ダイ・ハード」などに主演したハリウッド俳優は誰?': 'ブルース・ウィリス', 
'イルカが歌った「なごり雪」で、季節はずれの雪が降る都市はどこ?': '東京', 
'中国の三国時代で、三国に含まれていないのはどれ?': '隋(ずい)', 
'次のうち、画家ピカソの作品はどれ?': 'アビニョンの娘たち', 
'マルコ・ポーロの「東方見聞録」で「ジパング」と呼ばれていた国はどこ?': '日本', 
'特殊工作員として様々な任務を遂行するアクションゲームローグオプスの主人公は？': 'ニキ', 
'手紙や電報で、受取人自身に開封を求める言葉はどれ?': '親展', 
'漫画ベルサイユのばらで描かれている革命は？': 'フランス革命', 
'どんなラッシュでも電車の座席に座ることができるサラリーマンを描いた漫画流星課長の舞台になっている電車は？': '京王線', 
'次のうち、アニメ小公女セーラの中でセーラが大切にしていた人形の名前は？': 'エミリー', 
'日本酒の原料はどれ?': 'お米', 
'次のうち、さびる素材はどれ?': '鉄', 
'コーヒー豆の焙煎度で最も深煎りなのはどれ?': 'イタリアン・ロースト', 
'次のうち、スポーツはどれ?': '卓球', 
'1985年のアメリカ映画ＭＩＳＨＩＭＡで三島由紀夫を演じた俳優は？': '緒方拳', 
'おなじみの彫刻「考える人」の作者は誰?': 'ロダン', 
'カーリングの的となる円を何という？ ハウス': 'ハウス', 
'ソフトバンクグループのインターネット検索エンジンはどれ?': 'Yahoo! Japan', 
'「マスク」「プリンス」などの種類がある果物はどれ?': 'メロン', 
'クリミア戦争で活躍したナイチンゲールの職業はどれ?': '看護婦', 
'次のうち、自家用の軽自動車のナンバープレートの色はどれ?': '黄', 
'平成14年度にJAFロードサービスが出動した理由で最も多いものはどれ?': 'バッテリー上がり', 
'2005年10月に公開された映画あぶない刑事シリーズの最新作は？': 'まだまだあぶない刑事', 
'俗に森のバターとも呼ばれる果物といえば何？': 'アボカド', 
'多口のテーブルタップで複数の電気器具を使う時、コードが四方八方に延びている様子を何配線という？': '蛸足', 
'日本代表が銅メダルを獲得したメキシコ五輪のサッカーで金メダルを獲得した国は？': 'ハンガリー', 
'次のうち、国の数が最も多い地域はどれ?': 'アフリカ', 
'父「観阿弥」、子「世阿弥」が完成させた芸術はどれ?': '能', 
'紫式部が書いた源氏物語の第１帖のタイトルは？': '桐壺', 
'アメリカ五大湖のひとつであるこの湖は？最も西の湖': 'スペリオル湖', 
'江戸幕府の初代将軍は徳川家康ですが二代目の将軍は誰でしょう？': '徳川秀忠', 
'物質の状態変化で固体が液体に変化することを何という？': '融解', 
'女性歌手・松任谷由実の結婚前の苗字は？': '荒井', 
'サッカーの技術でヘディングシュートといえば体のどこで打つシュート？': '頭', 
'環境保全に役立つ商品につけられる「エコマーク」に書かれている言葉はどれ?': 'ちきゅうにやさしい', 
'都道府県の「府」があるのはどこ?': '近畿', 
'北向きの窓から外を見た時、正面に見えるのは、どの方角?': '北', 
'次のうち、女性が知事を務めている県はどれ?': '千葉県', 
'関西地方でまる鍋と呼ばれるのは、何が入った鍋料理？': 'すっぽん', 
'三村マサカズと、大竹一樹のお笑いコンビはどれ?': 'さまぁ～ず', 
'管弦楽、吹奏楽の最高音域を担当する管楽器はどれ?': 'ピッコロ', 
'次のうち、兵庫県にある島はどれ?': '淡路島', 
'全長2700kmに及ぶ、万里の長城を作らせた人物は誰?': '始皇帝', 
'1979年に公開された映画戦国自衛隊で戦国時代にタイムスリップした自衛隊が手を結ぶ武将は？': '長尾景虎', 
'2005年にブラジル人選手クリスチャンが入団したＪリーグのチームは大宮アルディージャですがドドが入団した入団したＪリーグのクラブは？': '大分トリニータ', 
'馬に胃袋は１つありますが牛に胃袋はいくつある？': '４つ', 
'ピッツバーグやフィラデルフィアがあるアメリカの州は？': 'ペンシルバニア州', 
'弘法大師と呼ばれた空海が、高野山に建てた寺はどれ?': '金剛峯寺', 
'次のうち、小泉総理大臣と同じ年齢の人物は誰?': '金正日総書記', 
'1860年、桜田門外の変で暗殺された幕府の大老は誰?': '井伊直弼', 
'サッカーは最後にドイツが勝つスポーツだ、という言葉は誰の言葉？': 'リネカー', 
'聖徳太子が制定した憲法は17条から成っていましたが北条泰時が制定した御成敗式目は何条から成っていた？': '51条', 
'室町時代、細川勝元と山名宗全が諸大名を巻き込んで争った戦いはどれ?': '応仁の乱', 
'日本銀行が市中銀行に貸し出しを行うときの金利を何という？': '公定歩合', 
'韓国の首都「ソウル」の名前の意味はどれ?': '都', 
'次のうち、外国で作られた曲はどれ?': 'トロイカ', 
'作家の武者小路実篤が1918年に宮崎県に作った理想郷の名前は？': '新しき村', 
'セルバンテスの小説ドン・キホーテでドン・キホーテが巨人と間違えたものは？': '風車', 
'次の道路標識のうち円形をしているのはどれ？': '駐車禁止', 
'時計の長針が15分間に動く角度は何度?': '90度', 
'ハツカネズミの名前の由来となった「二十日間」とは、何の日数?': '妊娠期間', 
'1867年に大政奉還をした将軍は誰?': '徳川慶喜', 
'童話「さるかに合戦」で最後にサルを攻撃するのはどれ?': 'うす', 
'次のうち、エジプトの首都はどれ?': 'カイロ', 
'アニメちびまる子ちゃんで花輪くんの家の運転手ヒデじいの本名は何？': '西城秀治', 
'大ヒット中のドラマ「HERO」の主演男優は誰?': '木村拓哉', 
'著しい経済成長を遂げており注目される４つの国を指した造語ＢＲＩＣｓに含まれないのはどれ？': 'イスラエル', 
'江戸時代後期から広まった福の神の人形「福助」の名字はどれ?': '叶(かのう)', 
'次のうち、キリスト教を保護した大名は誰?': '織田信長', 
'ベトナム料理の人気メニューでゴイクンといえば？': '生春巻き', 
'英語で「ソイ・ソース」と呼ばれる調味料はどれ?': 'しょうゆ', 
'1989年に採択された商標の国際登録制度確立のための議定書の名称は何議定書？': 'マドリード', 
'栃木なまりとあるあるネタでおなじみのピン芸人といえば誰？': 'つぶやきシロー', 
'セガのＰＳ２ゲーム龍が如くに登場する実在のショップは？': 'ドン・キホーテ', 
'文豪ゲーテの、臨終の言葉として伝えられているものはどれ?': 
'もっと光を', '現在、日本で発行されている紙幣で、最もサイズが大きいものはどれ?': '一万円札', 
'かつてファミコンを発売していたメーカーは？': '任天堂', 
'任天堂から発売されているシミュレーションゲームで聖戦の系譜烈火の剣などが発売されたシリーズは？': 'ファイアーエムブレム', 
'正六面体の面の形は正方形ですが正八面体の面の形は？': '正三角形', 
'1997年2月に誕生が公表されたクローン羊の名前はどれ?': 'ドリー', 
'体の部分を表す言葉でほぞといえばへそのことですがうなといえばどこのこと？': 'くび', 
'サッカーのポジションを表す「ボランチ」の、ポルトガル語の意味はどれ?': '舵取り', 
'作家ジョン・アーヴィングのベストセラー小説を原作とするジョディ・フォスターが主演した1986年公開の映画は？': 'ホテル・ニューハンプシャー', 
'富士五湖の1つ「本栖湖」が描かれているお札はどれ?': '五千円札',
'アニメおジャ魔女どれみで魔女ガエルに姿を変えたマジョリカが空を飛ぶときに使っているのは？': 'チリトリ', 
'次のうち、最も重いのはどれ?': '1貫', 
'「下戸」と呼ばれる人が飲めないものはどれ?': 'お酒', 
'次のうちキン肉マンの好物はどれ？牛丼': '天丼', 
'カクテキといえばどんな野菜を用いたキムチ？': 'ダイコン', 
'女王・卑弥呼が支配していた国はどこ?': '邪馬台国', 
'どじょうすくいで有名な安来節は島根県の民謡ですが斎太郎節はどの都道府県の民謡？': '宮城県', 
'古谷徹、銀河万丈、金田朋子らが所属する声優事務所といえば青二プロダクションですが野沢雅子、関俊彦、清水愛らが所属する声優事務所といえば？': '81プロデュース', 
'物理学者ロバート・フックはイギリスの人ですが生物学者レーウェンフックはどこの国の人？': 'オランダ', 
'ファッション雑誌an・anの名前の由来となった動物は？': 'ジャイアントパンダ', 
'ニコラス・ケイジが主演した2001年公開の恋愛映画はコレリ大尉の“何”？': 'マンドリン', 
'「サルスベリ」「モズ」を漢字で書いたとき、共通して使われる文字はどれ?': '百', 
'珍味として知られるフォアグラを取り去ったあとの鴨肉を何という？': 'マグレ', 
'「尊皇攘夷(そんのうじょうい)運動」が起こったのは何時代?': '江戸時代', 
'童謡「浦島太郎」の歌詞で、竜宮城の美しさを表現している言葉はどれ?': '絵にもかけない', 
'次のうち、「百薬の長」と呼ばれるのはどれ?': '酒', 
'砂おろしとも呼ばれおでんだねとしても人気のある加工食品は？': 'こんにゃく', 
'「忍びの里」として知られる「伊賀」があったのは現在の何県?': '三重県', 
'妊婦向け雑誌たまごクラブが2004年６月の特集から使い始めた出来ちゃった結婚の代わりとなる言葉といえば何？': '授かり婚', 
'2006年に長嶋茂雄・一茂親子のＣＭ初共演が話題になったテレビＣＭはどこの企業のもの？': '三菱ＵＦＪ信託銀行', 
'キエシロフスキー監督の映画トリコロール／白の愛の主演女優は？': 'ジュリー・デルピー', 
'次のうち、トルストイの小説の登場人物から名前がつけられたアクセサリーはどれ?': 'カチューシャ', 
'次のうち、賞味期限の表示を義務付けられていないものはどれ?': 'アイスクリーム', 
'1979年に公開された映画スーパーマンでスーパーマンを演じた俳優はクリストファー・リーブですがスーパーマンに恋する女性記者ロイス・レインを演じた女優は？': 'マーゴット・キダー', 
'容易にできることのたとえを、「何の手をひねる」という?': '赤子', 
'スポーツブランドフレッド・ペリーのマークに描かれている植物は？': '月桂樹', 
'証券取引所で有名な「ウォール街」がある、アメリカの都市はどこ?': 'ニューヨーク', 
'映画ダンデズ・ピークは、どんな出来事を描いた映画？': '火山の噴火', 
'次のうち日本で売られている牛肉の分類にないのは？': '洋牛', 
'次のうちトライアスロンで行わない種目はどれ？': 'カヌー', 
'鎌倉時代の武将北条実時が創立した貴重な図書を収蔵した施設は？': '金沢文庫', 
'次のうち「薩摩藩」出身の武士は誰?': '大久保利通', 
'アメリカでSpeed Racerというタイトルで放送され人気を集めた日本のＴＶアニメは？': 'マッハGoGoGo', 
'警察で使われる「うそ発見機」はどれ?': 'ポリグラフ', 
'次のうち、焼き豚はどれ?': 'チャーシュー', 
'もともと旅行かばん専門店として創設されたブランドはどれ?': 'ルイ・ヴィトン', 
'中華料理「チンジャオロースー」の「スー」の意味はどれ?': '細切り', 
'これを作る職人を主人公とした1999年のＮＨＫ朝の連ドラは？ 和菓子': 'あすか', 
'バイオリンの名曲「G線上のアリア」の作曲者は誰?': 'バッハ', 
'「ダイナマイト」の語源となった言葉の意味はどれ?': '力', 
'作家・森鴎外が卒業したのは東京大学の何学部?': '医学部', 
'つんく♂が製作総指揮を務めた2001年に公開されたオムニバス映画は？': '東京★ざんすっ', 
'江戸幕府の初代将軍といえば徳川家康ですが室町幕府の初代将軍といえば誰？': '足利尊氏', 
'世界競馬の最高峰・凱旋門賞で２着になったことでも知られる1999年のＪＲＡ年度代表馬は？': 'エルコンドルパサー', 
'日本の勲章のうち女性のみに与えられるものは？': '宝冠章', 
'古代エジプトでファラオと呼ばれたのは誰?': '国王', 
'演劇部に所属する女子高生たちの青春を描いた、チョーホフの戯曲にちなんだ吉田秋生の漫画は？': '桜の園', 
'ディズニーアニメでおなじみの「プーさん」とはどんな動物?': 'クマ', 
'スピルバーグ監督の映画「ジョーズ」で、人間を襲うサメの種類はどれ?': 'ホオジロザメ', 
'オリンピックで日本が獲得した金メダルのうち、通算獲得数が最も多い男子の競技はどれ?': '体操', 
'聖徳太子が摂政を務めた時の天皇は誰?': '推古天皇', 
'次のうち、大相撲の本場所が行われない都道府県はどこ?': '広島県', 
'１９６９年７月、初めて月面に降り立ったアポロ１１号の船長の名前は何でしょう？': 'アームストロング', 
'ヒット曲「カブトムシ」「ボーイフレンド」などで知られる大阪出身の女性シンガーは誰?': 'aiko', 
'将棋の７大タイトルの中でもっとも歴史が古いのは名人ですが最も新しく設立されたのは？': '竜王', 
'帝国主義時代のアフリカ分割でリビアを獲得した国はどこ？': 'イタリア', 
'ちゃんと名のつく芸能人でＫＡＢＡ．ちゃんがかつて所属していた音楽・ダンスユニットは何？': 'ｄｏｓ', 
'現在、都道府県知事の任期は何年?': '4年', 
'1582年、本能寺で織田信長を襲った武将は誰?': '明智光秀', 
'次のうち、ギリシア神話に登場する海の神はどれ?': 'ポセイドン', 
'2002年、島津製作所に勤める田中耕一さんが受賞したノーベル賞はどれ?': '化学賞', 
'インダス文明の遺跡「モヘンジョ・ダロ」がある国はどこ?': 'パキスタン', 
'田舎町を守る魔法分隊の副隊長ロギューネが主人公の伊都工平のファンタジー小説は？': '第61魔法分隊', 
'カプコンのアクションゲーム魔界村の流れを受け継いだＰＳ２のソフトは？': 'マキシモ', 
'「おしん」「おはる」などの品種がある野菜はどれ?': '大根', 
'徳川将軍家の家紋でおなじみの植物といえばどれ?': '葵', 
'ポプコムソフトが開発しPC-8801で発売されたＲＰＧサバッシュをデザインした落語家といえば？': '三遊亭円丈', 
'虹の7色に含まれない色はどれ?': '白', 
'漫画テニスの王子様で不二周助が通っている学校は？': '青春学園', 
'アイゼンハワー大統領の国務長官として活躍した巻き返し政策で知られるアメリカの政治家は？': 'ダレス', 
'英語で「ジェラシー」といえばどれ?': '嫉妬', 
'次のうち、植物油、卵、酢から作られる調味料はどれ?': 'マヨネーズ', 
'日本の男子バレーボール代表が現在までに唯一の金メダルを獲得したのは何大会？': 'ミュンヘン五輪', '人気の焼酎いいちこの産地は大分県ですが百年の孤独の産地は？': '宮崎県', 
'デンプンを加水分解する消化酵素は何？': 'アミラーゼ', 
'「敵に塩を送る」の故事で、塩を送った武将は誰?': '上杉謙信', '果物の品種で長十郎といえば梨ですが次郎といえば？': '柿', '予算を超えてしまうことをたとえて、足がどうなるという?': '出る', 'ペンギンを漢字で書くとどれ?': '人鳥', '最初の元号「大化」から現在の「平成」まで、日本の元号は全部でいくつ?': '247', '日本の宇宙開発事業団の略称はどれ?': 'NASDA', '三井住友銀行の略称をアルファベット４文字で何という？': 'ＳＭＢＣ', '原動機付自転車のエンジンは総排気量何cc以下?': '50cc', 
'京都パープルサンガに所属するＦＷ黒部光昭が2005年シーズンにレンタルで移籍したＪリーグのチームは？': 'セレッソ大阪', '江戸時代、孤島に漂着していたジョン万次郎を助けたのはアメリカのどんな船?': '捕鯨船', 
'御伽草子「浦島太郎」で、浦島太郎が亀と出会ったきっかけはどれ?': '釣り上げた', 'マラリアを媒介することで知られる蚊の種類といえば何？': 'ハマダラカ', '鎌倉幕府を開いた人物は誰?': '源頼朝', '次のうち、漢字で「木耳」と書く食材はどれ?': 'きくらげ', 
'1963年にアニメ鉄腕アトムの第１作が放送されたとき一社提供していたスポンサーは明治製菓ですがエイトマンが放送されたとき一社提供していたスポンサーは？': '丸美屋食品工業', 
'次のうち、俳優・加山雄三の祖先に当たる人物は誰?': '岩倉具視', 'ゲームパックマンの主人公パックマンは何色のキャラクター？': '黄色', '1866年に、坂本龍馬らの仲介によって薩摩藩が同盟を結んだ藩はどこ?': '長州藩', '読むと寿命が縮む新聞が夜中に配達されるという内容のつのだじろうのホラー漫画は恐怖新聞ですが何度殺しても生き返ってくる無気味な少女を描いた伊藤潤二のホラー漫画は？': '富江', '金髪のまだら狼の愛称で呼ばれたのは誰？': '上田馬之助', 
'センターの正面で行うバレーボールのクイックは何？': 'Ａクイック', '次のうち、使えなくなった日本の紙幣を再利用して作られているものはどれ?': 'トイレットペーパー', 
'次のうち、車の点滅式方向指示器はどれ?': 'ウインカー', '次のうち、聖徳太子が務めた役職はどれ?': '摂政', '有名企業などからのメールを装いカード番号など個人情報を不正に入手する、ネット上で問題になっている詐欺手法といえば何？': 'フィッシング', 
'かつて手塚治虫漫画全集を刊行した出版社はどこ？': '講談社', '明治35年、北海道で観測史上国内最低気温摂氏マイナス41度を記録した都市はどこ?': '旭川市', 
'まわりの責任を1人で負うことを「何をかぶる」という?': '泥', '東京オリンピックの開会式にちなんで出来た祝日はどれ?': '体育の日', 
'馬に胃袋はいくつある？': '１つ', 'ウルトラセブンの中でウルトラセブンは恒点観測員の何号として地球に訪れた？': '３４０号', 'ＮＴＴの３ケタの特殊番号で１１７といえば何の番号？': '時報', 'プロボクシングにおいて最も重い階級は？': 'ヘビー級', 
'オリックスのイチロー選手の出身高校はどこ?': '愛工大名電', '1986年のサッカーＷ杯を当初開催するはずだったが経済的な困難などを理由に辞退した南米の国は？': 'コロンビア', 'アニメサザエさんに登場するイクラちゃんの苗字は何？': '波野', 'オーストリア皇太子夫妻が暗殺されたことがきっかけで起こった戦争はどれ?': '第一次世界大戦', 
'パチスロ用語でRTといえば通常何の略のことを指す？': 'リプレイタイム', 'ヨーロッパ原産の犬「プードル」の胴回りの毛を刈り込む元々の目的は何?': '泳ぎやすくする', 'サッカーで、ボールを地面に落とさないように蹴り続けることを何という?': 'リフティング', '次のうち、江戸幕府で実際にあった役職はどれ?': '畳(たたみ)奉行', 'カナダの首都はどこ?': 'オタワ', '次のうち人気の焼酎“３Ｍ”に含まれないのは？': '萬膳', '漫画金色のガッシュ!!でガッシュとともに戦うパートナーは？': '高嶺清麿', '次のうち1973年にリリースされたあべ静江のヒット曲は？': 'コーヒーショップで', 
'読売ジャイアンツが本拠地としている東京ドームにつけられている愛称は？': 'ＢＩＧ\u3000ＥＧＧ', 
'チークダンスの「チーク」とはどれ?': 'ほほ', '「アジア太平洋経済協力会議」の略称はどれ?': 'APEC', '魚の「フグ」を漢字で書いたときにつかわれる文字はどれ?': '豚', 'バテレンといえば、次のどの宗教を伝来する為の宣伝師？': 'キリスト教', 'ドラマ木更津キャッツアイや氣志團の活躍で注目を集めた千葉県の木更津市はどこ？': '木更津', 'アメリカのクリントン大統領の一人娘の名前はどれ?': 'チェルシー', 'アニメ宇宙戦艦ヤマトの主題歌を歌ったのは誰？': 'ささきいさお', 
'漫画仮面の忍者赤影で主人公・赤影を従わせている戦国武将は？': '豊臣秀吉', 'コシヒカリの山地で有名な「魚沼」がある県はどこ?': '新潟県', '戦国時代、川中島の戦いで武田信玄と戦った武将は誰?': '上杉謙信', '赤塚不二夫の漫画もーれつア太郎の主人公ア太郎が営む家業は何？': '八百屋', 'キュリー夫人が発見した元素はどれ?': 'ラジウム', 
'じゃがいもを英語で言うとどれ?': 'ポテト', '日本の公営ギャンブルで競艇の監督省庁は？': '国土交通省', '出家以後は芳香院と号した戦国武将・前田利家の妻は？': 'まつ', 'ジャレコのアドベンチャーゲームミシシッピー殺人事件で片メガネとヒゲが特徴の名探偵といえば？': 'チャールズ', '聖徳太子が建立した法隆寺の別名はどれ?': '法隆学問寺', '次のうち、インド洋に発生する熱帯低気圧はどれ?': 'サイクロン', '漫画ONE PIECEに登場するトニートニー・チョッパーはどんな動物？': 'トナカイ', '指きりげんまんの「げんまん」の意味はどれ?': '一万年恨む', 
'英語で木曜日を表す言葉はどれ?': 'Thursday', '次の世界遺産のうち、奈良県にあるものはどれ?': '法隆寺', 'トルストイの小説戦争と平和のヒロインは？': 'ナターシャ', '第18回夏季五輪の開催地といえば東京ですが第18回冬季五輪の開催地といえばどこ？': '長野', '1955年に34歳で亡くなったジャズ界に革命を起こしバードにニックネームで呼ばれたサックス奏者は？': 'チャーリー・パーカー', '前漢の武帝によって中央アジアの大月氏に派遣され、西域の情報を持ち帰った外交家は誰？': '張驀', '2004年のアテネ五輪で日本人唯一の参加者が五十嵐俊幸といえばこの競技は何？': 'ボクシング', 
'「クリミアの天使」と呼ばれた人物は誰?': 'ナイチンゲール', '飲酒運転による罰金の最高額はいくら?': '50万円', '特撮ヒーロー「仮面ライダー」の原作者は誰?': '石ノ森章太郎', '次のうち、島崎藤村が創刊した雑誌はどれ?': '文学界', '日本の政党自由民主党をアルファベット３文字で表すと次のうちどれ？': 'ＬＤＰ', '「三国一の花嫁」などと例える時の三国は日本、中国ともう1つはどれ?': 'インド', 'かつて日清焼そばＵＦＯのＣＭでＵＦＯ仮面ヤキソバンを演じたのはマイケル富岡ですがケトラーを演じたのは？': 'デーブ・スペクター', 
'ケンタッキーフライドチキンの「カーネル・サンダース像」がしているネクタイはどれ?': 'リボンタイ', 'ドラマ北の国からの実際にはなかった副題は次のうちどれ？': '’８６卒業', 
'中国で問題になっている小胖子といったらどんな人のこと？': '太り過ぎの子', 
'杉浦日向子の漫画百日紅で描かれている江戸時代の有名な浮世絵師は？': '葛飾北斎', 
'世界遺産にも登録されている姫路城がある県はどこ?': '兵庫県', 
'プロレスラー・大谷晋二郎が持っているプロレスの教科書の１ページ目に載っている言葉は何？': 
'生涯志高く、今が奇跡なり！', 
'日本人選手がオリンピックで初めて金メダルを獲得した競技はどれ?': '陸上'
}}

    await client.ch.send("::q")

    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print(dateTime)
    print("今入ってる鯖の数"+str(server_number))


    loop.start()
    looop.start()

    channel_id_report = 629327961132236800
    print('We have logged in as {0.user}'.format(client))

    client.global_list = [] #グローバルチャット参加チャンネルのリスト
    for guild in client.guilds:
        tmp = discord.utils.get(guild.text_channels,name="global_yui")
        if tmp: client.global_list.append(tmp)


    embed = discord.Embed(title="YUI起動ログ",description="起動したよ",color=0x2ECC69)
    embed.set_thumbnail(url=random.choice(('https://yahoo.jp/box/3faN7k','https://yahoo.jp/box/c9L236','https://yahoo.jp/box/Jxj1Jd')))
    embed.add_field(name="起動時刻", value=str(dateTime.year)+"/"+str(dateTime.month)+"/"+str(dateTime.day)+"\n "+str(dateTime.hour)+"時"+str(dateTime.minute)+"分"+str(dateTime.second)+"秒", inline=False)
    embed.add_field(name="YUI news", value="大幅に改良！\n詳しくはヘルプの第６項から公式鯖へ", inline=True)

#    await asyncio.gather(*(c.send(embed=embed) for c in client.get_all_channels() if c.name == 'yui起動ログ'))

    embed = discord.Embed(title="YUI起動ログ",description="起動したよ",color=0x2ECC69)
    embed.set_thumbnail(url=random.choice(('https://yahoo.jp/box/3faN7k','https://yahoo.jp/box/c9L236','https://yahoo.jp/box/Jxj1Jd')))
    embed.add_field(name="起動時刻", value=str(dateTime.year)+"/"+str(dateTime.month)+"/"+str(dateTime.day)+"\n "+str(dateTime.hour+9)+"時"+str(dateTime.minute)+"分"+str(dateTime.second)+"秒", inline=False)
    await asyncio.gather(*(c.send(embed=embed) for c in client.get_all_channels() if c.name == '管理者用yui起動ログ'))




flag = False

yt_channel_id = CHANNEL_ID # 最初のチャンネルの



@tasks.loop(minutes=3)
async def check_last(): 
    tmp_timediff = datetime.datetime.now() - q_ch.last_message.created_at
    last_message_time = tmp_timediff.total_seconds()
    if last_message_time > 300: # もし最後のメッセージから5分以上経過していたら復帰する
        await q_ch.send("::q")


@tasks.loop(seconds=30)
async def loop():
    global yt_channel_id
    if flag:
        channel = client.get_channel(yt_channel_id)
        await channel.send('::atk loop')

    await client.change_presence(activity=discord.Game(name="y!help│"+str(len(client.guilds) )+'の鯖に所属中'))


@tasks.loop(seconds=60)
async def looop():
    now = datetime.datetime.now().strftime('%H:%M')
    if now == '00:01':

        print("時刻判定おｋ")

        em = discord.Embed(title="24:00の時報をお伝えします\nなんちゃって",description=random.choice((
'日付変わったから寝ようね！？',
'まだ起きてるとかみんな狂乱なの？',
'夜更かしは体に悪いよ……え、私？\nBOTだから支障ZEROですｗｗ',
'ねろ（辛辣\nさっさと寝ろ',
'別にいいけどさ……\n夜更かしは体壊さない程度にね',
'えーと、これ読めばいいの？ \n(台本ﾊﾟﾗﾊﾟﾗ)\nねえこの「お兄ちゃんもう寝ないと！」ってなに？\n殺されたいの？',
'私だって君が体壊したら悲しまないわけじゃないんだからさ\nちゃんと寝てね？\n私の事BOTだからってなめてるでしょ\nたとえプログラムされたコードで動いてるだけの義骸でも\n私は私なの')), inline=False)
        em.set_thumbnail(url="https://yahoo.jp/box/roWwt8")
        for c in client.get_all_channels():
            if c.name == 'yui時報ログ':
                client.loop.create_task(c.send(embed=em))
        print("チャンネル判定終了")

        login_ch = client.get_channel(643466975745540096)
        await login_ch.send('::login')

@client.event
async def on_disconnect():
    print("YUI was death")
    embed = discord.Embed(title="YUIが切断されあぁ！",description="原因は知らんけど切断されちゃった(灬ºωº灬)てへっ♡",color=0x2ECC69)
    embed.set_thumbnail(url=random.choice(('https://yahoo.jp/box/3faN7k','https://yahoo.jp/box/c9L236','https://yahoo.jp/box/Jxj1Jd')))
    embed.add_field(name="切断時刻", value=str(dateTime.year)+"/"+str(dateTime.month)+"/"+str(dateTime.day)+"\n "+str(dateTime.hour)+"時"+str(dateTime.minute)+"分"+str(dateTime.second)+"秒", inline=True)
#    await asyncio.gather(*(c.send(embed=embed) for c in client.get_all_channels() if c.name == 'yui起動ログ'))


@client.event
async def on_message(message):

#🔷test運用➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🔷

    if message.content == "y!help":
        help_embed_one = discord.Embed(title="YUIヘルプ目次━第１項",color=discord.Colour.green())
        help_embed_one.set_thumbnail(url=random.choice(('https://yahoo.jp/box/3faN7k','https://yahoo.jp/box/c9L236','https://yahoo.jp/box/Jxj1Jd')))

        help_embed_one.add_field(name="‣ヘルプ目次",value='━第１項',inline = True)
        help_embed_one.add_field(name="‣TAOコマンド",value='━第２項',inline = True)
        help_embed_one.add_field(name="‣メイン機能",value='━第３項',inline = True)
        help_embed_one.add_field(name="‣特殊チャンネル",value='━第４項',inline = True)
        help_embed_one.add_field(name="‣ガチャ",value='━第５頁',inline = True)
        help_embed_one.add_field(name="‣スロット",value='━第６頁',inline = True)
        help_embed_one.add_field(name="‣YUI関連URL",value='━第７頁',inline = True)
        help_embed_one.set_footer(icon_url=message.author.avatar_url, text=f"ヘルプ使用者│{message.author}")

        help_logch = client.get_channel(id = help_ch)
        embed=discord.Embed(title='ヘルプが開かれました',description=f'展開者│{message.author}\nＩ　Ｄ│{message.author.id}\n展開鯖│{message.author.guild}')
        await help_logch.send(embed=embed)
        page_count = 0 #ヘルプの現在表示しているページ数
        page_content_list = [
help_embed_0,
help_embed_one,
help_embed,
help_two_embed,
embed_special,
gacha,
slot_embed,
url_embed] #ヘルプの各ページ内容

        send_message = await message.channel.send(embed=page_content_list[0]) #最初のページ投稿
        await send_message.add_reaction("➡")

        def help_react_check(reaction,user):
            '''
            ヘルプに対する、ヘルプリクエスト者本人からのリアクションかをチェックする
            '''
            if reaction.message.id != send_message.id:
                return 0
            if reaction.emoji == "➡" or reaction.emoji == "⬅":
                if user != message.author:
                    return 0
                else:
                    return reaction,user

        while not client.is_closed():

            try:
                reaction,user = await client.wait_for('reaction_add',check=help_react_check,timeout=40.0)
            except:

                return #時間制限が来たら、それ以降は処理しない

            else:

                if reaction.emoji == "➡" and page_count < 8:
                    page_count += 1

                if reaction.emoji == "⬅" and page_count > 0:
                    page_count -= 1


                await send_message.clear_reactions() #事前に消去する
                await send_message.edit(embed=page_content_list[page_count])

                if page_count == 0:
                    await send_message.add_reaction("➡")
                elif page_count == 1:
                    await send_message.add_reaction("⬅")
                    await send_message.add_reaction("➡")
                elif page_count == 2:
                    await send_message.add_reaction("⬅")
                    await send_message.add_reaction("➡")
                elif page_count == 3:
                    await send_message.add_reaction("⬅")
                    await send_message.add_reaction("➡")
                elif page_count == 4:
                    await send_message.add_reaction("⬅")
                    await send_message.add_reaction("➡")
                elif page_count == 5:
                    await send_message.add_reaction("⬅")
                    await send_message.add_reaction("➡")
                elif page_count == 6:
                    await send_message.add_reaction("⬅")
                    await send_message.add_reaction("➡")
                elif page_count == 7:
                    await send_message.add_reaction("⬅")
                    await send_message.add_reaction("➡")
                elif page_count == 8:
                    await send_message.add_reaction("⬅")                    #各ページごとに必要なリアクション



    if message.content.startswith('y!kill'):
        if message.author.id == 446610711230152706:
            await client.logout()
            await sys.exit()
        else:
            embed = discord.Embed(title='権限がありません!!',description='これは開発者専用コマンドです')
            await message.channel.send(embed=embed)

#🔷➖➖➖➖➖➖➖➖➖➖オートアタック➖➖➖➖➖➖➖➖➖➖➖➖🔷


#🔷➖➖➖➖➖➖➖➖➖➖➖➖オートアタック改➖➖➖➖➖➖➖➖➖➖➖➖🔷
    global atk_ch_id
    global atk_ch
    global q_ch

    if message.content.startswith("y!atkch "):
        print('got the commond')
        atk_ch_id = message.content.split('y!atkch ')[1]
        atk_ch = discord.utils.get(message.guild.text_channels, mention=atk_ch_id)    
        await atk_ch.send(f"{message.author.mention}\nチャンネル指定完了\n`y!atk` てうってね")

                
    if f'{client.user.display_name}' in message.content:
        if description and "やられてしまった" in message.content:#🔷YUIの自動復活条件
            def  hellocheck(m):
                return m.content == "の攻撃" and m.author == message.author  and message.channel == m.channel#ここにメッセージが送られてきたチャンネル=最初のメッセージが送られてきたチャンネルという条件
            try:
                reply = await client.wait_for( "message" , check = hellocheck , timeout = 5.0 )
            except asyncio.TimeoutError:
                await atk_ch.send( "::i e 零-zero-" )
            else:
                await atk_ch.send( "::i e 壱-one-" )

        elif 'のHP' in message.content:
      
            def  hellocheck(m):
                return m.content == "の攻撃" and m.author == message.author  and message.channel == m.channel
            try:
                reply = await client.wait_for( "message" , check = hellocheck , timeout = 5.0 )
            except asyncio.TimeoutError:
                await atk_ch.send( "::atk **連+零-series+zero-**" )
            else:
                await atk_ch.send( "::atk **連+壱-series+one-**" )

        
    if message.content=='y!atkstop':
        atk_ch_id = '#tao-yui₀₀₀'
        atk_ch = discord.utils.get(message.guild.text_channels, mention=atk_ch_id)   



    if message.author.id == 526620171658330112 or message.author.id == 642271360667877386:
        
        if len(message.embeds) != 0:
            
            for embed in message.embeds:
                print(embed.to_dict())
                description = embed.description
                title = embed.title
                print('check a')
                if title and 'が待ち構えている' in title and message.channel==atk_ch:
                    print('check b')
                    await asyncio.sleep(5)
                    await atk_ch.send( "::atk 零-zero-" ) 
                    def  hellocheck(m):
                        return m.content == "攻撃失敗" and m.author == message.author  and message.channel == atk_ch
                    try:
                        reply = await client.wait_for( "message" , check = hellocheck , timeout = 5.0 )
                    except asyncio.TimeoutError:
                        await atk_ch.send("::atk 壱-one-")
                    else:
                        await atk_ch.send("::atk 弐-two-")
                else:
                    return

    if message.author.id == 526620171658330112 or message.author.id == 642271360667877386:
        
        if len(message.embeds) != 0:            
            for embed in message.embeds:                       
                if description and "このチャンネルの仲間全員が全回復した！" in description and message.channel==atk_ch:
                    def  hellocheck(m):
                        return  "PET" in description and m.author == message.author  and message.channel == atk_ch
                    try:
                        reply = await client.wait_for( "message" , check = hellocheck , timeout = 5.0 )
                    except asyncio.TimeoutError:
                        await atk_ch.send( "::atk　伍-five-" )
                    else:
                        await atk_ch.send( "::atk　陸-six-" )
                else:
                    pass 

                
    if message.author.id == 526620171658330112 or message.author.id == 642271360667877386:
        print("lv check")
        if len(message.embeds) != 0:             
            for embed in message.embeds:
                print("lv check 2")
                description = embed.description 
                print(embed.to_dict())
                if description and f'{client.user.mention}はレベルアップした！' in description : 
                    print('lv check 3')
                    level_up=description.split(f'{client.user.mention}はレベルアップした！')[1]
                    embed = discord.Embed(title=':lvup:',description = (level_up),color=discord.Colour.green())
                    embed.set_thumbnail(url="https://media.discordapp.net/attachments/635993816297504809/643091559142916109/videotogif_2019.11.10_23.14.46.gif?width=375&height=375")
                    embed.add_field(name="━時刻━", value=str(dateTime.year)+"/"+str(dateTime.month)+"/"+str(dateTime.day)+"/"+str(dateTime.hour)+"時"+str(dateTime.minute)+"分"+str(dateTime.second)+"秒", inline=False)

                    await asyncio.gather(*(c.send(embed=embed) for c in client.get_all_channels() if c.name == 'yuiレベルアップログ'))
                else:
                    print('not level up')  
                
    if message.author.id == 526620171658330112 or message.author.id == 642271360667877386:
        print("lv check　４")
        if len(message.embeds) != 0:             
            for embed in message.embeds:
                print("lv check ５")
                description = embed.description 
                if description and f'{client.user.mention}はレベルアップした！' in description : 
                    print('lv check ６')
                    level_up=description.split(f'{client.user.mention}はレベルアップした！')[1]
                    embed = discord.Embed(title=':lvup:',description = (level_up),color=discord.Colour.green())
                    embed.set_thumbnail(url="https://media.discordapp.net/attachments/635993816297504809/643091559142916109/videotogif_2019.11.10_23.14.46.gif?width=375&height=375")
                    embed.add_field(name="━時刻━", value=str(dateTime.year)+"/"+str(dateTime.month)+"/"+str(dateTime.day)+"/"+str(dateTime.hour)+"時"+str(dateTime.minute)+"分"+str(dateTime.second)+"秒", inline=False)

                    await asyncio.gather(*(c.send(embed=embed) for c in client.get_all_channels() if c.name == 'yuiレベルアップログ'))
                else:
                    print('not level up') 
                    
    #AIzaSyCKKWw8f4kvyNQbIe87XpC3A9FXLYKwrBM                
                    
                    
#🔷➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
    me = message.guild.me
    tao = client.ch.guild.get_member(526620171658330112)

    if message.content == "::q" and message.author == me:
        def quiz_check(tao_msg):
            if tao_msg.author != tao:
                return 0
            elif not tao_msg.embeds and not tao_msg.embeds[0].description:
                return 0
            elif tao_msg.embeds[0].author.name != "Quiz | ReYUI ver1.12.2#4984さんのクイズ":
                return 0
            return 1

        def ans_check(tao_msg):
            if tao_msg.author != tao:
                return 0
            elif not tao_msg.embeds and not tao_msg.embeds[0].description:
                return 0
            return 1
        
        try:
            quiz_msg = await client.wait_for("message",timeout=300,check=quiz_check)
        except asyncio.TimeoutError:
            await message.channel.send("::q")
            return

        quiz,*choice = quiz_msg.embeds[0].description.split("\n")
        true_choice = [word[4:] for word in choice]

        answer = client.already_quiz.get(quiz)
        await asyncio.sleep(4)

        react = 1
        if answer:
            react += true_choice.index(answer)        
        await quiz_msg.add_reaction(str(react).encode().decode('unicode-escape')+"\u20e3")

        try:
            ans_msg = await client.wait_for("message",check=ans_check)
        except asyncio.TimeoutError:
            await message.channel.send("::q")
            print(client.already_quiz)
            return

        tmp_embed = ans_msg.embeds[0].description
        if answer is None and not tmp_embed.startswith("時間切れ"):
            if tmp_embed.startswith("残念"):
                tmp = re.search("残念！正解は「(.*)」だ。",tmp_embed).group(1)
            elif tmp_embed.startswith("正解"):
                tmp = true_choice[0]
            client.already_quiz[quiz] = tmp

        await message.channel.send("::q")
        print(client.already_quiz)


#🔷➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🔷
    if message.author != client.user:
        reg_res = re.compile(u"y!wt (.+)").search(message.content)
        if reg_res:

          if reg_res.group(1) in citycodes.keys():

            citycode = citycodes[reg_res.group(1)]
            resp = urllib.request.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=%s'%citycode).read()
            resp = json.loads(resp.decode('utf-8'))

            msg = "🔹地域\n"
            msg += '```' + resp['location']['city']+'```'
            msg += '\n🔹天気\n'
            for f in resp['forecasts']:
              msg += '```' + f['dateLabel'] + ":" + f['telop'] + "```\n"

            embed = discord.Embed(title=msg,color = discord.Colour.blue())
            embed.set_thumbnail(url='https://yahoo.jp/box/J3FhL6')
            embed.set_author(name="🌐YUI WEATHER🌐")
            await message.channel.send(embed=embed)

          else:
            await message.channel.send( '・ω・)そんな場所知らんがなggrks')

#🔷➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🔷


    if message.content.startswith("y!clean "):

        reply = message.content.split('y!clean ')[1]


        if message.author.guild_permissions.administrator:
            await message.channel.purge(limit=int(reply))
            embed = discord.Embed(title="お掃除完了！！",description=(reply)+"のメッセージを消去したよ‪\n(꜆꜄꜆˙꒳˙)꜆꜄꜆ ｵﾗｵﾗ\n遅くなっちゃってごめんね\n(´・ω・`;)",
                                  color=0x2ECC69)
            embed.set_thumbnail(url="https://yahoo.jp/box/N0OpiM")
            await message.channel.send(embed=embed)

        else:
            embed = discord.Embed(title="権限エラー！！",description="管理者権限無しでチャンネル内のログ全部消せたら相当やばいよ私",
                                  color=0x2ECC69)
            embed.set_thumbnail(url="https://yahoo.jp/box/JAzR8X")
            await message.channel.send(embed=embed)

#🔷➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🔷


    if message.content.startswith("y!poll "):
        await message.delete()
        x = message.content.split(" ",2)
        r = x[1]
        re2 = x[2]
        embed = discord.Embed(title=(r),description=(re2),color=0x2ECC69)#https://i.pximg.net/img-original/img/2015/11/06/00/03/01/53402632_p0.png
        embed.add_field(name = "発言者",value = f"{message.author.mention}")
        embed.set_thumbnail(url=random.choice(('https://yahoo.jp/box/3faN7k','https://yahoo.jp/box/c9L236','https://yahoo.jp/box/Jxj1Jd')))
        embed.set_author(name="ReYUI ver1.12.2",url="https://discord.gg/nzS5GKM",icon_url="https://yahoo.jp/box/roWwt8")
        s = await message.channel.send(embed=embed)
        [await s.add_reaction(i) for i in ('👍', '👎')]  # for文の内包表記


    if message.content.startswith("y!say3 "):
        await message.delete()
        x = message.content.split(" ",2)
        e = x[1]
        re2 = x[2]
        embed = discord.Embed(title=(e)
        ,description=(re2)
        ,color=0x2ECC69)
        embed.add_field(name = "発言者",value = f"{message.author.mention}\n"+str(dateTime.year)+"/"+str(dateTime.month)+"/"+str(dateTime.day)+"\n "+str(dateTime.hour)+"時"+str(dateTime.minute)+"分"+str(dateTime.second)+"秒")
        await message.channel.send(embed=embed)

    if message.content.startswith("y!say2 "):
        await message.delete()
        x = message.content.split(" ",2)
        e = x[1]
        re2 = x[2]
        embed = discord.Embed(title=(e)
        ,description=(re2)
        ,color=0x2ECC69)
        await message.channel.send(embed=embed)

    if message.content.startswith("y!say1 "):
        await message.delete()
        reply_one = message.content.split('y!say1 ')[1]
        await message.channel.send(reply_one)


#🔷➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🔷


    if message.content.startswith("y!report "):

        await message.delete()

        embed = discord.Embed(title='レポート提出完了！',description=f"{message.author.mention}さん\nレポート提出有り難う！\n君のレポートは無事研究所に届けられたよ！",color=0x2ECC69)
        embed.add_field(name="レポート提出時刻", value=str(dateTime.year)+"/"+str(dateTime.month)+"/"+str(dateTime.day)+"\n "+str(dateTime.hour)+"時"+str(dateTime.minute)+"分"+str(dateTime.second)+"秒", inline=True)
        await message.channel.send(embed=embed)

    if message.content.startswith("y!report "):
        channel_id_report = 629327961132236800
        reply = message.content.split('y!report ')[1]
        embed = discord.Embed(title='レポート内容\n'+(reply),description=f"発言者{message.author.mention}",color=0x2ECC69)
        embed.add_field(name="レポート提出時刻", value=str(dateTime.year)+"/"+str(dateTime.month)+"/"+str(dateTime.day)+"\n "+str(dateTime.hour)+"時"+str(dateTime.minute)+"分"+str(dateTime.second)+"秒", inline=True)
        await asyncio.gather(*(c.send(embed=embed) for c in client.get_all_channels() if c.name == '【地下室】yuiレポート'))




    # 「すて」と発言したら「::st」が返る処理
    if message.content == 'y!st':
        await message.channel.send('::status window　私のステータスが見たいなんて、君もエッチだな')

    # 「りせ」と発言したら「::re」が返る処理
    if message.content == 'y!re':
        await message.channel.send('::reset')

    if message.content == 'y!atk':
#レスポンスされる運勢のリストを作成
        unsei = ["::atk　てい", "::atk　うりゃ", "::atk　とう", "::atk　はい", "::atk　ほい", "::atk　むん",]
        choice = random.choice(unsei) #randomモジュールでunseiリストからランダムに一つを選出
        await message.channel.send(choice)

    if message.content == 'y!i e':
        await message.channel.send('::i e')

    if message.content == 'y!i i':
        await message.channel.send('::i i \nまあこれもuser指定するのめんどくて作ってないから意味ないけどね')

    if message.content == 'y!i f':
        await message.channel.send('::i f')

    if message.content == 'よしよし':
        value=random.choice(('**………？**',
        '**そう何回もよしよしされたら私勘違いするよ……？**',
        '**セクハラ？**','**……君以外がやってたら殺してるよ**',
        '**なに急に……びっくりするじゃん。いやじゃないけどさ……**',
        '**ちょっと、やめてよ恥ずかしい**',
        '**……素直にありがとうって言えばいいの？**',
        '**？　よくわからないけど、お礼だけ言っておくわ。ありがとう**'))
        await message.channel.send(value)


    if message.content == 'よしよしヾ(・ω・｀)':
        await message.channel.send('''？　よくわからないけど、お礼だけ言っておくわ。ありがとう''')

   # 「まっぷ」と発言したら「::rmap」が返る処理
    if message.content == 'y!rmap':
        await message.channel.send('::rmap')

    # 「ろーる」と発言したら「::role」が返る処理
    if message.content == 'y!role':
        await message.channel.send('::role \nこれ一応作ったけどリアクションで役職選択させるのは\nめんどくさくてつくってないからほぼ意味ないんだよね……')

    # 「あいてむ」と発言したら「::i」が返る処理
    if message.content == 'y!i':
        await message.channel.send('::i')

    # 「ろぐいん」と発言したら「::login」が返る処理
    if message.content == 'y!login':
        await message.channel.send('::login')

    if message.content == 'y!join':
        role = discord.utils.get(message.guild.roles, name='裏寄生隊')#YUI通知
        await message.author.add_roles(role)
        reply = f'{message.author.mention} これで隊員の一人ね'
        await message.channel.send(reply)

    if message.content == 'y!announce':
        role = discord.utils.get(message.guild.roles, name='YUI通知')#YUI通知
        await message.author.add_roles(role)
        reply = f'{message.author.mention} 何か更新あったら呼ぶね'
        await message.channel.send(reply)




    if message.content == "y!kuji":
        # Embedを使ったメッセージ送信 と ランダムで要素を選択
        num_random = random.randrange(1,5)
        url1 = 'https://cdn.discordapp.com/attachments/635993816297504809/641195024033251328/29_20191105173957.png'
        url2 = 'https://cdn.discordapp.com/attachments/635993816297504809/641196128137904128/29_20191105174422.png'
        url3 = 'https://cdn.discordapp.com/attachments/635993816297504809/641197802436952065/29_20191105174815.png'
        url4 = 'https://cdn.discordapp.com/attachments/635993816297504809/641198139537227776/29_20191105175219.png'
        url5 = 'https://cdn.discordapp.com/attachments/635993816297504809/641200232826142730/29_20191105180042.png'
        await message.channel.send('くじ引いてく？')
        await asyncio.sleep(3)
        embed = discord.Embed(title="**ディスコ神社│御籤コーナー\n( 厂˙ω˙ )厂うぇーい**",description='''がさ
　がさ
　　がさ''',color=0x2ECC69)
        embed.add_field(name='**紙切れがでてきた…！！**',value='さあさあ今日の運勢は……!?')
        embed.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/635993816297504809/641207863506632715/28_20191105183055.png')
        embed.set_footer(icon_url=message.author.avatar_url, text=f"御籤使用者│{message.author.name}")
        if num_random == 1:
            embed.set_image(url = url1)
            await message.channel.send(embed=embed)
            await message.channel.send('お、大吉!!\nいいねいいね!!')

        elif num_random == 2:
            embed.set_image(url = url2)
            await message.channel.send(embed=embed)
            await message.channel.send('ん、小吉\nまあ凶とかよりはね…?')

        elif num_random == 3:
            embed.set_image(url = url3)
            await message.channel.send(embed=embed)
            await message.channel.send('ん...んん、末吉\nまぁまぁまぁ…ね?')

        elif num_random == 4:
            embed.set_image(url = url4)
            await message.channel.send(embed=embed)
            await message.channel.send('大凶!?\nえ、死ぬの!?')

        elif num_random == 5:
            embed.set_image(url = url5)
            await message.channel.send(embed=embed)
            await message.channel.send('すみませぇえええん\nこの御籤呪われてまあああああああす!!')


    if message.content == 'y!gacha':
        await message.channel.send('gachaばんごうをしていしてね......?')
        embed = discord.Embed(title="ガチャ機能だよ",description="コマンドはy!gacha [ガチャ番号]",color=0x2ECC69)
        embed.set_thumbnail(url="https://yahoo.jp/box/HYqbOS")
        embed.add_field(name="ガチャ種類＋番号一覧",value="‣__**通常ガチャ**　番号：1__\n色々よくわからないものが出てくるよ。\nたまに隠しコマンドが出てくるとかなんとか\n\n‣__**おにゃのこガチャ**　番号：2__\n可愛いおにゃのこの画像がいっぱいだよ\n可愛いの純度１００％！")
        await message.channel.send(embed=embed)


    if message.content == "y!gacha 1":
        embed = discord.Embed(title="あ、ガチャガチャじゃんまわしてみる？", description=f"""　　ﾁｬﾘｰﾝ
ｶﾞﾁｬｶﾞﾁｬｶﾞﾁｬ
　　　ﾎﾟﾝ！""",
                              color=0x2ECC69)
        embed.set_thumbnail(url="https://yahoo.jp/box/HYqbOS")
        embed.set_image(url=random.choice(("https://yahoo.jp/box/tpeHgW",
        "https://yahoo.jp/box/roWwt8","https://yahoo.jp/box/M8DDfm",
        "https://yahoo.jp/box/5yaQwS","https://yahoo.jp/box/snmtCk",
        "https://yahoo.jp/box/WI0bCW","https://yahoo.jp/box/2DeZEI",
        "https://yahoo.jp/box/seZwkN","https://yahoo.jp/box/UHhqck",
        "https://yahoo.jp/box/ZdKwTS","https://yahoo.jp/box/coBg_L",
        "https://yahoo.jp/box/D8lFL8","https://yahoo.jp/box/LU1JLi",
        "https://yahoo.jp/box/xfDFnC","https://yahoo.jp/box/2tGQPm",
        "https://yahoo.jp/box/2tGQPm","https://yahoo.jp/box/W6sq6m",
        "https://yahoo.jp/box/o8_WCa","https://yahoo.jp/box/bnadWl",
        "https://yahoo.jp/box/wvFtaX","https://yahoo.jp/box/t6DACy",
        "https://yahoo.jp/box/Iz8VoJ","https://yahoo.jp/box/QqiwDa",
        "https://yahoo.jp/box/XMZ_-6","https://yahoo.jp/box/HYqbOS",
        "https://media.discordapp.net/attachments/635993816297504809/636080181991178250/20_20191022145513.png",
        "https://media.discordapp.net/attachments/635993816297504809/636080191499927552/20_20191022145257.png")))
        embed.add_field(name=random.choice(('最高に需要無いんだけど……', 'うわ何これ……いる？', '……こんなのガチャガチャから出てこないよね普通', 'ごめんちょっと意味わからないんだけどナニコレ', "これもらって喜ぶ人いるのかな", '………ノーコメント')), value='YUIは出てきたものをそっとポッケに入れた', inline=False)
        await message.channel.send(embed=embed)

    if message.content == "y!gacha 2":
        embed = discord.Embed(title="おにゃ……のこ…ガチャ？　取り合えずまわしてみる？", description=f"""　　ﾁｬﾘｰﾝ

　ｶﾞﾁｬｶﾞﾁｬｶﾞﾁｬ

　　　　ﾎﾟﾝ！""",
                              color=discord.Colour.from_rgb(255,133,214))
        embed.set_thumbnail(url="https://yahoo.jp/box/lc5-cP")
        embed.set_image(url=random.choice(("https://yahoo.jp/box/C5OhZ6",
        "https://yahoo.jp/box/7wCPzz",
        "https://yahoo.jp/box/NTtrKt",
        "https://yahoo.jp/box/1lR9DJ",
        "https://yahoo.jp/box/uIdpqC",
        "https://yahoo.jp/box/YQlvC2",
        "https://yahoo.jp/box/sxklm2",
        "https://yahoo.jp/box/LpiAUS",
        "https://yahoo.jp/box/xkG1WU",
        "https://yahoo.jp/box/4T6wmr",
        "https://yahoo.jp/box/WEgd7D",
        "https://yahoo.jp/box/6VLJXh",
        "https://yahoo.jp/box/yDuiFh",
        "https://yahoo.jp/box/gtay8J",
        "https://yahoo.jp/box/-zJbpA",
        "https://yahoo.jp/box/xH_xpw",
        "https://yahoo.jp/box/KQDNjd",
        "https://yahoo.jp/box/XT5J4M",
        "https://yahoo.jp/box/AoWqBP",
        "https://yahoo.jp/box/3CKNvk",
        "https://yahoo.jp/box/pFKU2Z",
        "https://yahoo.jp/box/nH4vvY",
        "https://yahoo.jp/box/cqTkgv",
        "https://yahoo.jp/box/kvCkil",
        "https://yahoo.jp/box/rvDbkR",
        "https://yahoo.jp/box/znUdy5",
        "https://yahoo.jp/box/wmzu-Z",
        "https://yahoo.jp/box/kXnYQf",
        "https://yahoo.jp/box/0cRE1S",
        "https://yahoo.jp/box/Mz2rPI",
        "https://yahoo.jp/box/JzZEBY",
        "https://yahoo.jp/box/o1Uma1",
        "https://yahoo.jp/box/YPaIEe",
        "https://yahoo.jp/box/MANLfg",
        "https://yahoo.jp/box/e09Dte",
        "https://yahoo.jp/box/iFQl2O",
        "https://yahoo.jp/box/EjWQbT",
        'https://yahoo.jp/box/3faN7k',
        'https://yahoo.jp/box/c9L236',
        'https://yahoo.jp/box/Jxj1Jd')))
        embed.add_field(name=random.choice(('いや可愛いけどコメントに困る', 'あ、かわいい', 'ちょくちょくエッチなのは入ってるよねこれ（）', '可愛いというより萌えのほうが正しいのかなこれ', "普通にかわいいこれ", 'あー悪くないかも')), value='YUIは出てきたおにゃのこカードをそっとポケットに仕舞った', inline=False)
        await message.channel.send(embed=embed)





#🔷アイコン表示系コード➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🔷



    if message.content == "y!myicon":
        embed = discord.Embed(title="**アイコン表示**\n",description = '`アイコンを表示したよ`',color=discord.Color(random.randint(0, 0xFFFFFF)))
        embed.set_image(url=message.author.avatar_url_as(size=1024))
        embed.set_footer(icon_url=message.author.avatar_url, text=f"表示者│{message.author}")
        await message.delete()
        await message.channel.send(embed=embed)

#🔷サイコロ系コード➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🔷



    if message.content.startswith("y!dice "): #ここの!diceは好きなのにしていいぞ
        if client.user != message.author:
            x = message.content.split(" ",2)
            dice = x[1]
            dice2 = x[2]
            num_random = random.randrange(int(dice),int(dice2))
            embed = discord.Embed(title="ゆいがサイコロ振るだけ",description='''指定範囲は'''+(dice)+'から'+(dice2)+'!!\n'+'''なにがでるかなー

**__　'''+str(num_random)+''' __**٩( 'ω' )و!!''',color=0x2ECC69)
            await message.channel.send(embed=embed)


    if message.content.startswith("y!nekoshima"): #ここの!diceは好きなのにしていいぞ
        if client.user != message.author:
            num_random = random.randrange(1,10000)
            embed = discord.Embed(title="YUIの超激レア占い",description='''次の超激レア枠は～!!
**'''+str(num_random)+'''**体後!!　がんばー٩( 'ω' )و''',color=0x2ECC69)
            embed.set_thumbnail(url=random.choice(('https://yahoo.jp/box/3faN7k',
        'https://yahoo.jp/box/c9L236',
        'https://yahoo.jp/box/Jxj1Jd')))
            await message.channel.send(embed=embed)


    if 'おつ' in message.content or '乙' in message.content or 'ｵﾂ' in message.content or 'オツ' in message.content:
        if message.author.bot:
           pass

        else:
            channel = message.channel
            oha = random.choice(('(\*´ω｀*)ｵﾂｶﾚｻﾏー','‪(꜆꜄꜆˙꒳˙)꜆꜄꜆ ｵﾂｵﾂｵﾂ‬','( 厂˙ω˙ )厂うぇーい','おつかれさまぁ～  (\*ˊ˘ˋ*)♪','おつおつ( ´꒳`)','おつ(　ˆᴘˆ　)'))

            await channel.send(oha)



    if 'オハ' in message.content or 'ｵﾊ' in message.content or 'oha' in message.content or 'おは' in message.content:
        if message.author.bot:

             return

        else:
            channel = message.channel
            oha = random.choice(('おはー(((o(\*ﾟ▽ﾟ*)o)))','(ฅ・ω・ฅ)おはよう♪','⸜(\* ॑꒳ ॑*  )⸝⋆*オハ','おは(　ˆᴘˆ　)'))

            await channel.send(oha)



    if 'おやす' in message.content or 'スヤァ' in message.content or 'oyas' in message.content or 'ｽﾔｧ' in message.content or 'ねる' in message.content or '寝る' in message.content:
        if message.author.bot:

             return

        else:
            channel = message.channel
            oha = random.choice(('( ˘ω˘ ) ｽﾔｧ…','( ˘꒳​˘ )ｵﾔｽﾔｧ…','_([▓▓] ˘ω˘ )_ｽﾔｧ…','=͟͟͞( ˘ω˘)˘ω˘)˘ω˘)ｼﾞｪｯﾄｽﾄﾘｰﾑｽﾔｧ…','ｽﾔｧ…(　ˆᴘˆ　)'))

            await channel.send(oha)




#🔷ログ系コード➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🔷

    if message.content.startswith("y!yui"):
        if message.content.split()[1] == "log":
            category_id = message.channel.category_id
            category = message.guild.get_channel(category_id)
            new_channel = await category.create_text_channel(name='yui起動ログ')
            reply = f'{new_channel.mention} をつくったよ。私が起きたら此処で挨拶するから'
            return await message.channel.send(reply)

        elif message.content.split()[1] == "timelog":
            category_id = message.channel.category_id
            category = message.guild.get_channel(category_id)
            new_channel = await category.create_text_channel(name='yui時報ログ')
            reply = f'{new_channel.mention} をつくったよ。日付が変わるタイミングでここでお知らせするから'
            
        
        elif message.content.split()[1] == "global":
            category_id = message.channel.category_id
            category = message.guild.get_channel(category_id)
            new_channel = await category.create_text_channel(name='global_yui')
            reply = f'{new_channel.mention} をつくったよ。globalチャットに登録完了'
            return await message.channel.send(reply)
#🔷➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖🔷

    if message.content == "y!timer":
        await message.delete()
        tmp = await message.channel.send("10") # 編集するメッセージを保持
        await asyncio.sleep(1)
        await tmp.edit( content = "9" )
        await asyncio.sleep(1)
        await tmp.edit( content = "8" )
        await asyncio.sleep(1)
        await tmp.edit( content = "7" )
        await asyncio.sleep(1)
        await tmp.edit( content = "6" )
        await asyncio.sleep(1)
        await tmp.edit( content = "5" )
        await asyncio.sleep(1)
        await tmp.edit( content = "4" )
        await asyncio.sleep(1)
        await tmp.edit( content = "3" )
        await asyncio.sleep(1)
        await tmp.edit( content = "2" )
        await asyncio.sleep(1)
        await tmp.edit( content = "1" )
        await asyncio.sleep(1)
        await tmp.edit( content = "0" )

    if message.content == "y!gorogoro":
        await message.delete()
        tmp = await message.channel.send("(:3\_ヽ)_......") # 編集するメッセージを保持
        await asyncio.sleep(1)
        await tmp.edit( content = "(:3\_ヽ)_......ねむいい......" )
        await asyncio.sleep(1)
        await tmp.edit( content = ".　( ε: )" )
        await asyncio.sleep(1)
        await tmp.edit( content = ".　　　(.ω.)" )
        await asyncio.sleep(1)
        await tmp.edit( content = ".　　　　　( :3 )" )
        await asyncio.sleep(1)
        await tmp.edit( content = ".　　　　  　('ω')" )
        await asyncio.sleep(1)
        await tmp.edit( content = ".　　　　 　　　(:3\_ヽ)_...." )
        await asyncio.sleep(3)
        await tmp.edit( content = ".　　　　　　　　 　(:3\_ヽ)_....なにがしたかったんだろ" )



    if message.content == "y!amanohashi":
        await message.delete()
        await message.channel.send("私の生みの親だね。まあどうでもいいけどね！")



    if message.content == "y!slot s":
        kakuritu = random.randint(1, 50)
        slot_list = [':eggplant:', ':cherries:', ':large_orange_diamond:', ':large_blue_diamond:', ':seven:',':gem:',':bell:',':eggplant:',':eggplant:',':eggplant:']
        A = random.choice(slot_list)
        B = random.choice(slot_list)
        C = random.choice(slot_list)
        if int(kakuritu) == int(1): #確率は1/50に設定（出来てるはず）
            await message.channel.send("これは何かが起こる予感…Σ(ﾟ□ﾟ；)\n\n\n")
            A = slot_list[4]
            B = slot_list[4]
            C = slot_list[4]
            await asyncio.sleep(3) #3秒間待ってやる
            embed = discord.Embed(title="YUIスロット スマホver\n"+" ┏━┳━┳━┓\n┃"+"%s┃%s┃%s┃\n ┗━┻━┻━┛" % (A, B, C),color=0x2ECC69)
            embed.add_field(name="スリーセブン！！！",value="ついてるねー")
            await message.channel.send(embed = embed)

        elif A == B and B == C and A == ':seven:':
            embed = discord.Embed(title="YUIスロット スマホver\n"+" ┏━┳━┳━┓\n┃"+"%s┃%s┃%s┃\n ┗━┻━┻━┛" % (A, B, C),color=0x2ECC69)
            embed.add_field(name="スリーセブン！！！",value="ついてるねー\nなかなかすごいよ")
            await message.channel.send(embed = embed)

        elif A == B and B == C and A == ':eggplant:':
            embed = discord.Embed(title="YUIスロット スマホver\n"+" ┏━┳━┳━┓\n┃"+"%s┃%s┃%s┃\n ┗━┻━┻━┛" % (A, B, C),color=0x2ECC69)
            embed.add_field(name="very KI☆TA☆NA☆I！！",value="汚らわしいねーｗ")
            await message.channel.send(embed = embed)

        elif A == B and B == C and A == ':bell:':
            embed = discord.Embed(title="YUIスロット スマホver\n"+" ┏━┳━┳━┓\n┃"+"%s┃%s┃%s┃\n ┗━┻━┻━┛" % (A, B, C),color=0x2ECC69)
            embed.add_field(name="三連ベル！！",value="いいねー")
            await message.channel.send(embed = embed)

        elif A == ':cherries:' and B != ":cherries:" and C != ":cherries:":
            embed = discord.Embed(title="YUIスロット スマホver\n"+" ┏━┳━┳━┓\n┃"+"%s┃%s┃%s┃\n ┗━┻━┻━┛" % (A, B, C),color=0x2ECC69)
            embed.add_field(name="単チェリー！！",value="ヨキヨキ")
            await message.channel.send(embed = embed)

        elif A == ':bell:' and B != ":bell:" and C != ":bell:":
            embed = discord.Embed(title="YUIスロット スマホver\n"+" ┏━┳━┳━┓\n┃"+"%s┃%s┃%s┃\n ┗━┻━┻━┛" % (A, B, C),color=0x2ECC69)
            embed.add_field(name="単ベル！！",value="(ノ・ω・)ノオオオォォォ-")
            await message.channel.send(embed = embed)


        elif A == B and B == C :
            embed = discord.Embed(title="YUIスロット スマホver\n"+" ┏━┳━┳━┓\n┃"+"%s┃%s┃%s┃\n ┗━┻━┻━┛" % (A, B, C),color=0x2ECC69)
            embed.add_field(name="BINGO！！！",value="ついてるねー")
            await message.channel.send(embed = embed)

        else:
            tmp = await message.channel.send("10") #    　


            embed = discord.Embed(title="YUIスロット スマホver\n"+" ┏━┳━┳━┓\n┃"+"%s┃%s┃%s┃\n ┗━┻━┻━┛" % (A, B, C),color=0x2ECC69)
            embed.add_field(name="残念……",value="もっかいやる？")
            await message.channel.send(embed = embed)


    if message.content == "y!slot c":
        kakuritu = random.randint(1, 50)
        slot_list = [':eggplant:', ':cherries:', ':large_orange_diamond:', ':large_blue_diamond:', ':seven:',':gem:',':bell:',':eggplant:',':eggplant:',':eggplant:']
        A = random.choice(slot_list)
        B = random.choice(slot_list)
        C = random.choice(slot_list)
        if int(kakuritu) == int(1): #確率は1/50に設定（出来てるはず）
            await message.channel.send("これは何かが起こる予感…Σ(ﾟ□ﾟ；)\n\n\n")
            A = slot_list[4]
            B = slot_list[4]
            C = slot_list[4]
            await asyncio.sleep(3) #3秒間待ってやる
            embed = discord.Embed(title="YUIスロット PCver\n"+" ┏━━┳━━┳━━┓\n┃"+" %s ┃ %s ┃ %s ┃\n ┗━━┻━━┻━━┛" % (A, B, C),color=0x2ECC69)
            embed.add_field(name="スリーセブン！！！",value="ついてるねー")
            await message.channel.send(embed = embed)

        elif A == B and B == C and A == ':seven:':
            embed = discord.Embed(title="YUIスロット PCver\n"+" ┏━━┳━━┳━━┓\n┃"+" %s ┃ %s ┃ %s ┃\n ┗━━┻━━┻━━┛" % (A, B, C),color=0x2ECC69)
            embed.add_field(name="スリーセブン！！！",value="ついてるねー\nなかなかすごいよ")
            await message.channel.send(embed = embed)

        elif A == B and B == C and A == ':eggplant:':
            embed = discord.Embed(title="YUIスロット PCver\n"+" ┏━━┳━━┳━━┓\n┃"+" %s ┃ %s ┃ %s ┃\n ┗━━┻━━┻━━┛" % (A, B, C),color=0x2ECC69)
            embed.add_field(name="very KI☆TA☆NA☆I！！",value="汚らわしいねーｗ")
            await message.channel.send(embed = embed)

        elif A == B and B == C and A == ':bell:':
            embed = discord.Embed(title="YUIスロット PCver\n"+" ┏━━┳━━┳━━┓\n┃"+" %s ┃ %s ┃ %s ┃\n ┗━━┻━━┻━━┛" % (A, B, C),color=0x2ECC69)
            embed.add_field(name="三連ベル！！",value="いいねー")
            await message.channel.send(embed = embed)

        elif A == ':cherries:' and B != ":cherries:" and C != ":cherries:":
            embed = discord.Embed(title="YUIスロット PCver\n"+" ┏━━┳━━┳━━┓\n┃"+" %s ┃ %s ┃ %s ┃\n ┗━━┻━━┻━━┛" % (A, B, C),color=0x2ECC69)
            embed.add_field(name="単チェリー！！",value="ヨキヨキ")
            await message.channel.send(embed = embed)

        elif A == ':bell:' and B != ":bell:" and C != ":bell:":
            embed = discord.Embed(title="YUIスロット PCver\n"+" ┏━━┳━━┳━━┓\n┃"+" %s ┃ %s ┃ %s ┃\n ┗━━┻━━┻━━┛" % (A, B, C),color=0x2ECC69)
            embed.add_field(name="単ベル！！",value="(ノ・ω・)ノオオオォォォ-")
            await message.channel.send(embed = embed)


        elif A == B and B == C :
            embed = discord.Embed(title="YUIスロット PCver\n"+" ┏━━┳━━┳━━┓\n┃"+" %s ┃ %s ┃ %s ┃\n ┗━━┻━━┻━━┛" % (A, B, C),color=0x2ECC69)
            embed.add_field(name="BINGO！！！",value="ついてるねー")
            await message.channel.send(embed = embed)

        else:
            embed = discord.Embed(title="YUIスロット PCver\n"+" ┏━━┳━━┳━━┓\n┃"+" %s ┃ %s ┃ %s ┃\n ┗━━┻━━┻━━┛" % (A, B, C),color=0x2ECC69)
            embed.add_field(name="残念……",value="もっかいやる？")
            await message.channel.send(embed = embed)


    if message.content == 'y!sinfo':

        guild = message.guild
        role = next(c for c in guild.roles if c.name == '@everyone')
        t_locked = 0
        v_locked = 0
        online = 0
        offline = 0
        idle = 0
        dnd = 0
        pin = 0
        if guild.mfa_level == 0:
            mfamsg = "メンバーに2要素認証を必要としていません"
        else:
            mfamsg = "メンバーに2要素認証を必要としています"
        if guild.premium_subscription_count == None:
            pmmc = "0"
        else:
            pmmc = guild.premium_subscription_count
        for member in guild.members:
            if member.status == discord.Status.online:
                online += 1
            if member.status == discord.Status.offline:
                offline += 1
            if member.status == discord.Status.idle:
                idle += 1
            if member.status == discord.Status.dnd:
                dnd += 1
        for channel in guild.text_channels:
            if channel.overwrites_for(role).read_messages is False:
                t_locked += 1
        for channel in guild.voice_channels:
            if channel.overwrites_for(role).connect is False:
                v_locked += 1
        total = online+offline+idle+dnd
        if total > 499:
            large = "大"
        elif total > 249:
            large = "中"
        else:
            large = "小"
        embed = discord.Embed(title=f"サーバー情報", color=0x2ECC69)
        embed.set_thumbnail(url=guild.icon_url)
        embed.add_field(name="‣サーバー名", value=f"**{guild.name}**",inline=False)
        embed.add_field(name="‣サーバーの説明", value=f"**{guild.description}**",inline=False)
        embed.add_field(name="‣サーバーID", value=f"**{guild.id}**")

        embed.add_field(name="‣サーバーの大きさ", value=f"**{large}**")
        embed.add_field(name="‣サーバー地域", value=f"**{guild.region}**")
        embed.add_field(name="‣サーバーの旗", value=f"**{guild.banner}**")
        embed.add_field(name="‣オーナー", value=f"**{guild.owner.mention}**",inline=False)
        embed.add_field(name="‣チャンネル数", value=f"総合チャンネル数　:**{len(guild.text_channels)+len(guild.voice_channels)}個**(🔒×**{t_locked+v_locked}**)\nテキストチャンネル:**{len(guild.text_channels)}個**(🔒×**{t_locked}**)\nボイスチャンネル　:**{len(guild.voice_channels)}個**(🔒×**{v_locked}**)")
        embed.add_field(name="‣カテゴリー数", value=f"**全て:{len(guild.categories)}**")
        embed.add_field(name="‣役職数", value=f"**{len(guild.roles)}職**",inline=False)
        embed.add_field(name="‣メンバー数", value=f"総メンバー:**{total}人**\nオンライン:**{online}人**\nオフライン:**{offline}人**\n退席中　　:**{idle}人**\n取り込み中:**{dnd}人**",inline=False)
        embed.add_field(name="‣サーバーのブースト状態", value=f"サーバーブーストレベル　:**Lv.{guild.premium_tier}**\nサーバーブーストユーザー:**{pmmc}人**",inline=False)
        embed.add_field(name="‣二段階認証", value=f"**{mfamsg}**",inline=False)
        await message.channel.send(embed=embed)

#🔷➖➖➖➖➖➖➖➖global chat space➖➖➖➖➖➖➖➖🔷



    if (len(message.embeds) == 0) and (message.channel.name == "global_yui") and (not "discord.gg" in message.author.name):
        content = re.sub(r"(https://discord.gg/)([a-zA-Z./%=]*)", r"||\1\2||", message.content)
        embed = discord.Embed(title=f'送信者│{message.author}',description=f"{content}",color=discord.Color(random.randint(0, 0xFFFFFF)))
        embed.set_thumbnail(url = message.author.avatar_url)
        embed.set_author(icon_url=message.guild.icon_url, name=f"{message.guild.name}")
        embed.set_footer(icon_url=client.user.avatar_url, text=f"YUI global chat system")
        await message.delete()
        for guild in client.guilds:
            for channel in guild.channels:
                if channel.name == "global_yui":
                    await channel.send(embed=embed)

    if message.content.startswith("y!mkch "):
        await message.delete()
        reply_one = message.content.split('y!mkch ')[1]
        category_id = message.channel.category_id
        category = message.guild.get_channel(category_id)
        new_channel = await category.create_text_channel(name=reply_one)
        reply = f'{new_channel.mention} を作成したよ!'

        await message.channel.send(reply)

    if message.content.startswith('y!send '):

        await message.delete()
        x = message.content.split(" ",2)
        riptext2 = int(x[2])
        channel = client.get_channel(riptext2)
        riptext = x[1]

        await channel.send(riptext)


    if client.user != message.author:
        kakuritu = random.randint(1, 20)
        if int(kakuritu)== 1:
            Z = ['あんぱん','メロンパン','フランスパン','チョコパイ']
            A = random.choice(Z)
            AZ = ['チョコ','粒あん','バター','しゃけ','ケチャップ']
            B = random.choice(AZ)
            C = ["知り合い","友達","マックで見かけた人","モスで見かけた人","たまたま電車で乗り合わせた人"]
            CC = random.choice(C)
            random_dana = ['お腹すいたなぁ…','ねえ\nだいぶ前に'+(CC)+'がやってたんだけど…'+(A)+'って'+(B)+'とあうの?','**プリン**に**醤油**をかけると**うにの味**って言うけど\nこれ式で表すと\n__**プリン味＋醤油味=うに味**__\nだよね\nじゃあさ、この式から\n__**うに味－醤油味=プリン味**__\nってことになるよね。\nつまりうにから醤油系の味成分を抽出しまくればいつかプリン味になるのかな!....?','フランスにはtaoという名前のペットボトル飲料がある','( 厂˙ω˙ )厂うぇーい','''＿人人人人人人人人＿\n＞ 突　然　の　死 ＜\n￣^Y^Y^Y^Y^Y^Y^Y￣''','(((((((((((っ･ω･)っ ｳｪｰｲ♪','| ε:)   にゅ','(^ω^≡^ω^).','( ˙꒳​˙  )ﾌｧｯ','|ω・)ﾐﾃﾏｽﾖ','(  ﾟཫ ﾟ)ｺﾞﾌｯ']
            text_random = random.choice(random_dana)
            await message.channel.send(text_random)
            print('selected')

    if client.user != message.author and message.author.bot:
    	if 'だよ' in message.content:
            aaa = ["そうなの？","そうだよ(便乗)"]
            AAA = random.choice(aaa)
            await message.channel.send(AAA)
    	if 'した' in message.content:
    	    await message.channel.send('そうなんだ...(困惑)')
    	if 'なの' in message.content and '？' in message.content:
    		await message.channel.send('そうだよ(便乗)')

    if client.user != message.author:
    	if 'くえー' in message.content:
    		y1 = ['……結構恥ずかしいからねこれ','…ごめん自分で反応しといてあれだけど、結構恥ずい','……はずいわ!','\nいやぁぁこれ言うの恥ずかしいからいやぁぁぁ','……それ言われたら反応しないといけないからやめて','\nなんでこんな恥ずいのに私が反応しなきゃ行けないの…']
    		y2 = random.choice(y1)
    		await message.channel.send('く、くえー…'+(y2))

    if client.user != message.author:
    	if 'ねこ' in message.content:
    		y1 = ['ねこですよろしくおねがいします','ねこはいましたよろしくおねがいします','ねこはいます','ねこはいました','ねこはどこにでもいます','ねこはここにいます']
    		y2 = random.choice(y1)
    		await message.channel.send((y2))
    if client.user != message.author:
    	if 'せやな' in message.content:
    		y1 = ['そやな']
    		y2 = random.choice(y1)
    		await message.channel.send((y2))

    if client.user != message.author:
    	if 'うぃ' in message.content or 'うぇ' in message.content:
    		y1 = ['( 厂˙ω˙ )厂うぇーい']
    		y2 = random.choice(y1)
    		await message.channel.send((y2))
    if client.user != message.author:
    	if 'くさ' in message.content or '草' in message.content:
    		y1 = ['w','www','草','𐤔𐤔𐤔','ʬ﻿ʬʬ﻿','෴෴']
    		y2 = random.choice(y1)#(　＾ω＾)おっおっおっ
    		await message.channel.send((y2))
    	if 'おっ' in message.content:
    		y1 = ['(　＾ω＾)おっおっおっ','( ˙꒳​˙    ≡   ˙꒳​˙  )おっおっおっ','(　＾ω＾)ｵｯw']
    		y2 = random.choice(y1)
    		await message.channel.send((y2))

    if client.user != message.author:
    	if 'ぽ' in message.content or 'ポ' in message.content:
    		y1 = ['㌼㌨㌥㌑㌝㌈㌏㌐　㌞㌞㌞㌞㌑㌆']
    		y2 = random.choice(y1)
    		await message.channel.send((y2))

    if client.user in message.mentions: # 話しかけられたかの判定
        embed = discord.Embed(title = 'YUI Information',description = f'{client.user}\nID 627052576810074112')
        embed.set_author(name=client.user,url="https://discordapp.com/api/oauth2/authorize?client_id=627052576810074112&permissions=8&scope=bot",icon_url=client.user.avatar_url)
        embed.set_footer(icon_url=message.author.avatar_url, text=f"表示者｜{message.author}")
        await message.channel.send(embed = embed)

        
            
client.run(TOKEN)

