# -*- coding: utf-8 -*-
"""Story: the emperor 100
"""
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')

from storybuilder.builder import world as wd
from src.emperor100 import config as cnf


# episodes
def ep_intro(w: wd.World):
    h, lion, milea, garneth = w.hero, w.lion, w.milea, w.garneth
    scenes = [
            w.scene("父の帰還",
                w.tag.comment("ここで簡単な世界観説明"),
                h.be(w.stage.castle, w.day.returnemp),
                h.look(w.stage.balcony, "父の帰還"),
                h.talk(milea, "父の功績"),
                milea.talk(h, "次の皇帝"),
                h.look(milea, w.child),
                h.be(w.i.throne, "次期皇帝"),
                h.be("皇帝の息子"),
                ),
            w.scene("継承の不安",
                h.go(w.stage.hall, "父を出迎え"),
                lion.come("here"),
                lion.talk(h, "孫の無事を確認"),
                lion.feel(w.i.badcondition.flag()),
                h.ask(w.i.peace_nego),
                lion.reply("上々"),
                garneth.come(),
                h.look(garneth, w.i.pope),
                h.think(w.i.pope, "マルダ教の最高司祭"),
                garneth.ask(lion, "ちょっと用件が"),
                h.look(lion, garneth, "行ってしまう"),
                ),
            w.scene("父の死去",
                lion.be("dead"),
                garneth.talk(h, lion, w.i.badcondition.deflag()),
                h.think(w.i.lion_dead.flag()),
                garneth.talk(h, w.i.enthrone),
                h.know(w.i.throne),
                ),
            ]
    return [w.chaptertitle("皇帝の死"),
            *scenes,
            ]


def ep_preparation(w: wd.World):
    h, milea, garneth = w.hero, w.milea, w.garneth
    scenes = [
            w.scene("父の死、皇帝の死",
                h.be(w.stage.castle, w.day.dead),
                garneth.talk(h, w.i.throne),
                h.be(w.i.throne, "$must"),
                h.know(w.i.lion_dead),
                h.talk(garneth, w.i.throne),
                garneth.talk(h, "日程や心得"),
                h.remember(w.i.emperor_bug.flag()),
                garneth.go("出ていく"),
                h.think("今後のこと"),
                ),
            w.scene("継承のこと",
                h.be(w.stage.hisroom),
                h.be(w.i.throne, w.i.emperor100),
                h.remember(w.i.lion_word),
                h.talk("彼女を呼んでくれ"),
                ),
            w.scene("母殺しの疑惑",
                h.remember(w.i.murder_mam),
                h.talk(milea, w.i.emperor_bug),
                milea.ask(h, "あなた私を殺すと？"),
                h.reply("自信がない"),
                milea.talk(h, "あなたを信じています"),
                milea.talk(w.child, "この子もいるし"),
                h.think(w.i.lion_word),
                h.know(w.i.milea_mind),
                h.look(w.child),
                ),
            w.scene("そして儀式を迎える",
                h.do("wake", w.day.ceremony),
                h.look(w.i.moon),
                h.think(w.i.moon, "凶事の象徴"),
                ),
            ]
    return [w.chaptertitle("儀式の準備"),
            *scenes,
            ]


def ep_ceremony(w: wd.World):
    h, milea, garneth, child = w.hero, w.milea, w.garneth, w.child
    scenes = [
            w.scene("儀式前",
                h.be(w.stage.hisroom, w.day.ceremony),
                h.think("whether", w.i.throne),
                milea.come("here"),
                h.ask(milea, "即位が恐ろしい"),
                milea.behav(h, "抱きしめる"),
                milea.talk(h, "本当は強い人よ"),
                h.talk(milea, "最愛の者を殺してもか？"),
                milea.talk(h, "それが神の示される運命なら受け入れます"),
                h.be(w.i.ceremony, "時間が迫る"),
                h.do(w.i.his_mind),
                ),
            w.scene("儀式",
                w.hero.do(w.i.enthrone),
                h.be("戴冠"),
                garneth.talk(h, "第百代皇帝"),
                w.people.talk("祝福"),
                garneth.talk(h, w.i.emp_ceremony),
                h.go(garneth, "二人だけで", w.stage.cathedral),
                ),
            w.scene("秘密の地下室へ",
                h.go(w.stage.cathedral),
                garneth.talk("王家代々継承時のみ入ることを許可されている"),
                h.look("秘密の部屋"),
                h.go("秘密の通路"),
                h.think("見た記憶がある"),
                ),
            w.scene("人格の継承",
                h.look(w.stage.lab),
                garneth.talk(h, "継承を始める"),
                h.do("薬を打たれる"),
                h.talk("何を"),
                garneth.talk("皇帝の人格を継承する"),
                h.ask("そのような魔術を？"),
                garneth.talk("太古のヒトの技術です"),
                garneth.talk("代々技術者の家系だった"),
                garneth.talk("人格の継承"),
                w.hero.be(w.i.portchara, "強制的に"),
                ),
            w.scene("最愛殺し",
                h.be(w.stage.hisroom),
                garneth.ask(h, "お目覚めですか？"),
                h.ask(garneth, "儂は皇帝か？"),
                garneth.reply("yes"),
                garneth.deal(h, w.tsword),
                h.go(milea, "彼女の居室"),
                milea.ask("お目覚めですね？"),
                h.deal("殺害"),
                w.hero.do(w.milea, "殺害", w.i.emperor_bug.deflag()),
                ),
            w.scene("呪いの継承",
                h.know(garneth, w.i.lion_dead.deflag()),
                h.look(child),
                h.talk(child, "お前もいずれ最愛の者を殺す"),
                ),
            ]
    return [w.chaptertitle("百代目のバグ"),
            *scenes,
            ]


# main
def world():
    w = wd.World("100 characters")
    w.set_db(cnf.CHARAS, cnf.STAGES, cnf.DAYS, cnf.ITEMS, cnf.INFOS, cnf.FLAGS)
    return w


def story(w: wd.World):
    return (w.maintitle("皇帝百代の呪（バグ）"),
            ep_intro(w),
            ep_preparation(w),
            ep_ceremony(w),
            )


def main(): # pragma: no cover
    w = world()
    return w.build(story(w))


if __name__ == '__main__':
    import sys
    sys.exit(main())

