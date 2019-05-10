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
                h.be(w.stage.apart, w.day.current),
                h.do("phone", w.osaki, "原稿締め切り", w.stage.indream),
                h.do("wake", "メール着信音"),
                h.deal(fuyumi, "普段メールよこさない彼女から", THM["2"]),
                h.do("返信しない"),
                h.hear("再度着信音"),
                h.look("押入れの中から"),
                h.look(w.terminal, THM["3"]),
                h.have(w.terminal),
                h.deal(w.fear_mail, THM["1"]),
                h.do("write", "$must"),
                h.do("write", w.i.novel),
                ),
            w.scene("未来人の隣人",
                h.hear("インタフォン"),
                h.look(fuyumi),
                h.ask(fuyumi, "ごめんまだメール見てない"),
                ft_fuyumi.talk("何のこと？"),
                h.look(ft_fuyumi, "冷たく豹変", THM["4"]),
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
                h.be("dead"),
                ),
            ]
    return [w.chaptertitle("これ以上書けない"),
            *scenes,
            ]


def ep_end(w: wd.World):
    h, osaki = w.hero, w.osaki
    scenes = [
            w.scene("走馬灯",
                h.remember("小学生のプールで溺れかけたのが最初", THM["5"]),
                h.think("死んだ理由は過労だった", THM["79"]),
                h.think("彼女の優しい嘘", "本当はもう限界だった", THM["76"]),
                h.look("桜の木の下での告白", THM["73"]),
                h.remember("こどもの日の約束だった", THM["14"]),
                h.think("それから始まった同居", THM["71"]),
                ),
            w.scene("過去の自分",
                h.be("dead"),
                h.deal(w.terminal, "時間を巻き戻せる", THM["13"]),
                h.go("過去に戻る", w.day.schoolday),
                h.go(w.stage.school),
                h.meet(w.pastman),
                h.look("空", THM["88"]),
                # TODO
                h.know("ずっと見守ってくれていた", THM["94"]),
                h.know(w.i.absencemaster.deflag(), "神だった", THM["77"]),
                ),
            w.scene("寝落ち！？",
                h.do("wake", "風呂", THM["72"]),
                h.think("神に会ってから一年", THM["25"]),
                h.be("目覚めたらアイデア", THM["86"]),
                ),
            w.scene("走る",
                h.go(w.stage.bar, "向かう"),
                h.think("一冊の本を出すのがどれだけ大変か", THM["89"]),
                h.think("あの日捨てたちんけなプライド", THM["85"]),
                ),
            w.scene("小説を書く意味",
                h.go(w.stage.bar),
                osaki.talk("待ってた", THM["90"]),
                h.meet(osaki, THM["87"]),
                h.have("新しい小説の企画", THM["93"]),
                osaki.feel("原稿のぬくもり", THM["92"]),
                h.know(w.i.his_reason),
                h.look("グラスの氷がとける", THM["98"]),
                h.know("100回目の企画会議", THM["100"]),
                h.be("未解決テーマ",
                    THM["29"],
                    THM["30"],
                    THM["31"],
                    THM["32"],
                    THM["33"],
                    THM["36"],
                    THM["37"],
                    THM["38"],
                    THM["39"],
                    THM["40"],
                    THM["41"],
                    THM["42"],
                    THM["43"],
                    THM["44"],
                    THM["45"],
                    THM["46"],
                    THM["47"],
                    THM["48"],
                    THM["49"],
                    THM["50"],
                    THM["63"],
                    THM["64"],
                    THM["65"],
                    THM["66"],
                    THM["67"],
                    THM["68"],
                    THM["69"],
                    THM["70"],
                    THM["74"],
                    THM["75"],
                    THM["78"],
                    THM["80"],
                    THM["81"],
                    THM["82"],
                    THM["83"],
                    THM["84"],
                    THM["91"],
                    THM["95"],
                    THM["96"],
                    THM["97"],
                    THM["99"],
                    ),
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

