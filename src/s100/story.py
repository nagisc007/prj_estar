# -*- coding: utf-8 -*-
"""Story program for My mystery by my side.
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.s100 import config as cnf
THM = cnf.THEMES


# episodes
def ep_intro(w: wd.World):
    h, osaki, fuyumi, ft_fuyumi = w.hero, w.osaki, w.fuyumi, w.ft_fuyumi
    scenes = [
            w.scene("追い詰められた作家の苦悩",
                w.tag.comment("主人公の人間性紹介と彼女との状況設定"),
                w.tag.comment("主人公の一人称"),
                h.do("write").d("書く",
                    "という行為は時に狂気を孕んでいる",
                    "と$meなんかは思う"),
                h.talk().t("あぁもう！",
                    "何だよお題「１００」で小説一本書けってのはよお"),
                h.be(w.stage.apart, w.day.current).d("視界を思い切りパソコンのモニタから天井",
                    "そして狭苦しいアパートの玄関へと移動させると",
                    "スチール製のドアが申し訳なさそうに開くのを目撃した"),
                h.deal(fuyumi, "普段メールよこさない彼女から", THM["2"]).t("……ごめん"),
                h.look().d("聞き取れないほどの声でそう言って入ってきたのは",
                    "同棲してこの春で三年目になる$fuyumiだった"),
                h.talk().t("何か忘れ物か？",
                    "それともまた仕事嫌になったから戻ってきたのか"),
                h.look().d("義姉のスナックの手伝いに散々嫌気が差しているらしいが",
                    "それでも生活資金の為と日々苦手な化粧をしては出かけていく。",
                    "そんな彼女の背を見送る度に自分の不甲斐なさに泣きたくなるが",
                    "いつかは立派な作家先生として店で一番高い酒を頼んでやるつもりだ"),
                fuyumi.come().d("彼女は何も言わないままドアを閉めると",
                    "そのまま上がってきてコートを脱いだ"),
                h.do("phone", w.osaki, "原稿締め切り", w.stage.indream).d("ちょうどそのタイミングで携帯電話が鳴り出す"),
                h.do("wake", "メール着信音").t("あ、はい", "もしもし$myです"),
                h.think().d("相手は編集の$na_osakiだった。",
                    "内容は案の定原稿の締め切りの話で",
                    "パソコンの画面にはまだ一行しか書けていなかったが",
                    "百枚の原稿の既に半分は終わっていると上手く誤魔化しておいた"),
                h.reply().t("はいはい", "大丈夫ですって",
                    "$meのこと信用してないんですか？"),
                h.think().d("そりゃあ何度も原稿を落としたことのある底辺作家を信頼なぞ出来ないだろう"),
                h.talk().t("え？",
                    "あの$na_nishikawaですか？",
                    "彼が直川賞候補に……そうですか"),
                h.do("返信しない").d("$nishikawaは同じ新人賞出身の作家だったが",
                    "今やＴＶにも顔出しをする人気作家になってしまった"),
                h.deal().d("プレッシャーを掛けるつもりだったのだろうが",
                    "ただ気落ちさせただけだということを伝える気力すらないまま",
                    "$meは$na_osakiからの電話を切った"),
                fuyumi.talk().t("$hero……"),
                h.ask().t("何だよ$her"),
                h.look().d("彼女は真っ赤な唇にお化けのようなアイシャドウでじっと見下ろしたまま",
                    "手にしたスマートフォンをただ差し出す"),
                h.talk().t("それがどうかしたのか？"),
                h.look("押入れの中から"),
                h.look(w.terminal, THM["3"]).d("だがよく見れば彼女のスマホにしては何ともゴテゴテとデコレーションされている。",
                    "おまけに画面が虹色に閃いたかと思うと、"),
                h.talk().t("あん！？"),
                h.hear("再度着信音").d("それは女の泣き声のような音をかき鳴らした"),
                h.have(w.terminal),
                h.deal(w.fear_mail, THM["1"]).d("見ればどうやらメールが着信しただけらしいが、"),
                h.ask().t("なあ$her。",
                        "これって誰のだ？"),
                h.do("write", "$must").d("そこには差出人が空白のまま"),
                h.look().t("百個のお題全てを使って小説を書かなければ大切なものを失う"),
                h.do("write", w.i.novel).d("と書かれていた"),
                fuyumi.talk().t("だから作家になるなんて夢さっさと捨てれば良かったのよ！"),
                h.reply().t("ふ、$her？"),
                h.look(ft_fuyumi, "冷たく豹変", THM["4"]).d("突然声を上げた彼女はいつも一つに括っている髪を振り乱してこちらを向くと",
                        "般若の面のモデルにでもなったかのように目を剥き出しにして",
                        "こう言った"),
                fuyumi.talk().t("それね",
                        "底辺作家に届く呪いのメールなんだよ！",
                        "実際に店に来てた先生がそれ貰ったって笑ってた次の日から全然来なくなって",
                        "そしたら一月後に心筋梗塞で亡くなってたんだから……"),
                ),
            w.scene("未来人の隣人",
                h.hear("インタフォン"),
                h.look(fuyumi),
                h.ask(fuyumi, "ごめんまだメール見てない"),
                ft_fuyumi.talk("何のこと？"),
                ft_fuyumi.ask("中に入れてくれない？"),
                ),
            ]
    return [w.chaptertitle("冒頭"),
            *scenes,
            ]


def ep_middle(w: wd.World):
    h, fuyumi, ft_fuyumi = w.hero, w.fuyumi, w.ft_fuyumi
    scenes = [
            w.scene("もう一人の冬美",
                ft_fuyumi.explain(h, "隣に越してきた", THM["8"]),
                h.think("自分にはもったいない完璧", "ちぐはぐなカップル", THM["26"]),
                h.look(ft_fuyumi),
                ft_fuyumi.talk("相談"),
                h.know(ft_fuyumi, w.ichioku, THM["7"]),
                h.remember(fuyumi, "機械音痴", THM["11"]),
                h.know(ft_fuyumi, w.i.future_mail, THM["12"]),
                ),
            w.scene("学生時代",
                h.remember(w.day.schoolday),
                h.be(w.i.lostmemory, THM["19"]),
                h.meet(ft_fuyumi, "あの時の女性"),
                h.deal(w.terminal, "時間を戻る"),
                h.be("透明人間として", THM["17"]),
                h.come("秋の学校", THM["10"]),
                h.do("教室の戸を開けると初恋の彼女", THM["6"]),
                ft_fuyumi.talk("ずっと待ってる", THM["18"]),
                h.think("その約束が全ての始まり", THM["9"]),
                h.think("誰にも言わない秘密のはずだった", THM["28"]),
                ),
            w.scene("現在の自分は",
                h.have("コーヒーと煙草", THM["20"]),
                h.remember("当時は言えなかった秘密の趣味＝妄想小説", THM["21"]),
                h.think("あの頃のキラキラがない", THM["22"]),
                h.remember("あの時を思い出すと恥ずかしい", THM["15"]),
                h.have(w.nishikawa, "著作"),
                h.think("同期", "面白くて悔しい", THM["23"]),
                ),
            w.scene("未来からの警告",
                h.be(w.stage.apart, w.day.current),
                h.think(w.i.future_mail),
                h.have(fuyumi, w.i.fuyumi_call),
                h.talk(fuyumi, "別離"),
                h.talk("説得", fuyumi),
                h.look(fuyumi, "自分の小説", "彼女に自分の才能を示す"),
                h.have(w.i.help_mail, "助けて", THM["24"]),
                h.look("未来の自分からだった", THM["27"]),
                ),
            ]
    return [w.chaptertitle("展開"),
            *scenes,
            ]


def ep_climax(w: wd.World):
    h = w.hero
    scenes = [
            w.scene("未来からの指示",
                ),
            w.scene("外出",
                h.go(w.stage.subway, THM["51"]),
                h.go(w.stage.sea, THM["52"]),
                h.go(w.stage.bookstore, THM["53"]),
                h.go(w.stage.school),
                ),
            w.scene("望んでいた過去",
                h.go(w.stage.school, "文化祭", THM["54"]),
                h.think("当時はSNSなんてなく", THM["55"]),
                h.feel("初恋は何も言わずに終わった", THM["57"]),
                h.look("学生時代のアルバム", THM["56"]),
                ),
            w.scene("ありえた現在",
                h.go(w.stage.conveni, THM["58"]),
                h.look("動画が流れる", THM["60"]),
                h.look("夫婦で働く姿", THM["59"]),
                h.hear("夢だったと語る彼ら", THM["61"]),
                ),
            w.scene("悲しい現実",
                h.come(w.stage.bar, "神屋", THM["62"]),
                h.have("極上の突き出し", THM["35"]),
                h.think(w.i.absencemaster.flag(), THM["34"]),
                ),
            w.scene("そして自分が死ぬ",
                h.be(w.stage.apart, w.day.current),
                h.think(w.i.help_mail),
                h.do("help", w.futureman),
                h.know(w.futureman, "dead"),
                h.do(w.futureman, "小説を書く"),
                h.think("この世の終わりだ", THM["16"]),
                h.remember("小さい頃夜空に願った", THM["49"]),
                h.be("dead"),
                h.think("世界が真夜中になった", THM["82"]),
                ),
            ]
    return [w.chaptertitle("これ以上書けない"),
            *scenes,
            ]


def ep_end(w: wd.World):
    h, osaki, fuyumi = w.hero, w.osaki, w.fuyumi
    scenes = [
            w.scene("走馬灯",
                h.remember("小学生のプールで溺れかけたのが最初", THM["5"]),
                h.think("死んだ理由は過労だった", THM["79"]),
                h.think("彼女の優しい嘘", "本当はもう限界だった", THM["76"]),
                h.look("桜の木の下での告白", THM["73"]),
                h.have("桜の花びらをくれた", THM["44"]),
                h.remember("こどもの日の約束だった", THM["14"]),
                h.think("それから始まった同居", THM["71"]),
                h.think("すぐ夏がきた", THM["81"]),
                fuyumi.talk("夏なんてなくなればいいのに", THM["31"]),
                h.talk("気になるやつ（作家）がいるんだ", THM["80"]),
                h.think("それに彼女は嫉妬した", THM["63"]),
                h.think("久々のデートが雪の夜に", THM["69"]),
                h.think("小さなこたつで二人", THM["67"]),
                fuyumi.talk("バレンタイン大嫌い", THM["68"]),
                h.look("半分に割れたチョコ", THM["50"], THM["43"]),
                h.think("最悪な誕生日", THM["47"]),
                h.think("その日のおかえりはなかった", THM["29"]),
                fuyumi.talk("ごめんなさい", "最後の言葉", THM["46"]),
                ),
            w.scene("過去の自分",
                h.be("dead"),
                h.deal(w.terminal, "時間を巻き戻せる", THM["13"]),
                h.go("過去に戻る", w.day.schoolday),
                h.think("だから幸福を取り戻す時間の旅に出た", THM["30"]),
                h.go(w.stage.school),
                h.meet(w.pastman),
                fuyumi.talk("またね", THM["42"]),
                h.remember("まだ気持ちが繋がっていると思っていた頃"),
                fuyumi.talk("悲鳴", THM["41"]),
                h.think("何度やり直しても死ぬ"),
                h.look("割れた彼女のメガネ", THM["40"]),
                h.think("疲れたもういやだ", THM["39"]),
                h.talk("もうやめてやる", THM["32"]),
                h.look("一匹の猫だった", THM["38"]),
                h.look("空", THM["88"]),
                h.think("小説日和だ", THM["99"]),
                h.look("真っ青が広がる", THM["83"]),
                h.know("ずっと見守ってくれていた", THM["94"]),
                h.know(w.i.absencemaster.deflag(), "神だった", THM["77"]),
                h.think("神からのお返し？", THM["97"]),
                h.do("眠りに落ちた", THM["75"]),
                h.hear("おやすみ", THM["36"]),
                ),
            w.scene("寝落ち！？",
                h.look("目を開けると", THM["37"]),
                h.do("wake", "風呂", THM["72"]),
                h.think("神に会ってから一年", THM["25"]),
                h.be("目覚めたらアイデア", THM["86"]),
                ),
            w.scene("走る",
                h.go(w.stage.bar, "向かう"),
                h.think("一冊の本を出すのがどれだけ大変か", THM["89"]),
                h.think("あの日捨てたちんけなプライド", THM["85"]),
                h.remember("彼女にさよならされた理由", THM["84"]),
                fuyumi.talk("今日は特別な日だったのに", THM["70"]),
                h.think("雨の日に別れた", THM["78"]),
                ),
            w.scene("小説を書く意味",
                h.go(w.stage.bar),
                h.think("トンデモ上司がいた", THM["33"]),
                osaki.talk("ギリギリだな", THM["45"]),
                osaki.talk("待ってた", THM["90"]),
                osaki.talk("二人で最強パーティだろ？", THM["64"]),
                h.ask("チョコじゃないんですか？", THM["95"]),
                h.talk("お年玉で父にプレゼントしたんです", THM["66"], THM["65"]),
                h.meet(osaki, THM["87"]),
                h.have("新しい小説の原稿", THM["93"]),
                h.look("タイトルは「ぬくもりの感染」", THM["48"]),
                h.look("真っ白", THM["91"]),
                osaki.talk("今でも忘れてないぞお前の最初の原稿", THM["74"]),
                h.talk("となりにいつも小説の神様いるんで", THM["98"]),
                osaki.feel("原稿のぬくもり", THM["92"]),
                h.know(w.i.his_reason),
                h.look("グラスの氷がとける", THM["96"]),
                h.know("100回目の企画会議", THM["100"]),
                ),
            ]
    return [w.chaptertitle("最後の作品"),
            *scenes,
            ]


# main
def world():
    w = wd.World("100 stories project")
    w.set_db(cnf.CHARAS, cnf.STAGES, cnf.DAYS, cnf.ITEMS, cnf.INFOS)
    return w


def story(w: wd.World):
    return [w.maintitle("百妄想騙り"),
            ep_intro(w),
            ep_middle(w),
            ep_climax(w),
            ep_end(w),
            ]


def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

