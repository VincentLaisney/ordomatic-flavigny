# coding: utf-8

import datetime

from various import hebdo_psalterii_inv, is_third_week_of_september

'''
Voici la liste des fêtes propres à Flavigny:
27 avril: Dédicace de la cathédrale Saint-Bénigne
7 septembre: solennité de sainte Reine (P. Vianney serait favorable à la célébrer comme mémoire mineure à Solignac)
19 septembre: mémoire mineure de saint Seine
8 novembre: mémoire de sainte Élisabeth de la Trinité dans le diocèse de Dijon. Mais comme elle vient d’être inscrite au propre de France, rien n’empêche désormais de célébrer sa mémoire à Solignac également.
13 novembre: fête de saint Bénigne
25 novembre: mémoire de sainte Catherine Labouré
'''

def dict_flav_create(current_year, even_year, dict_tempo):
    dict_flav = {}

    dedicace_dijon_date = datetime.date(current_year, 4, 27)
    dedicace_dijon = dict_flav[dedicace_dijon_date] = {}
    dedicace_dijon["force"] = 70
    dedicace_dijon["header"] = "\\textbf{\\textsc{In Dedicatione Ecclesiæ Cathedralis Divionensis}} - \\textbf{festum} - \\textit{Alb.}"
    dedicace_dijon[
        "body"] = "\n\\item Omnia de Communi dedicationis ecclesiæ ritu paschali: in fine cuiuslibet responsorii, ante versum, additur \\textit{Alleluia} nisi iam habeatur.\n\\item \\textit{In ML: præfatio in dedicatione ecclesiæ \\emph{(Gloria, Credo)}.}\n\\item In MC: Missa de Communi dedicationis ecclesiæ (MR 895); lectiones propriæ: Apoc \\textbf{21}, 1-5a / Io \\textbf{2}, 13-22; præfatio in dedicatione ecclesiæ II."

    sainte_reine_date = datetime.date(current_year, 9, 7)
    sainte_reine = dict_flav[sainte_reine_date] = {}
    sainte_reine["force"] = 100
    sainte_reine[
        "I_vesp"] = "\\item I Vesperæ sollemnitatis sequentis. ¶ \\textit{Adiuvabit eam} et versiculum in AM 1178."
    # Si tombe un dimanche, on calcule quel dimanche (per annum, post Pentecosten).
    # if sainte_reine_date.weekday() == 6:
    #     num_dim_ap_pentec = (sainte_reine_date - pentecote).days // 7
    #     num_dim_per_annum = f_roman_numbers(
    #         num_dim_ap_pentec + 35 - nb_dim_ap_pentec)
    #     num_summer = " - " + \
    #         f_num_summer(sainte_reine_date)[
    #             0] + f_num_summer(sainte_reine_date)[1]
    #     text_ap_pentec = f_roman_numbers(
    #         num_dim_ap_pentec) + " post Pentecosten" + num_summer
    #     text_dim = " \\textbf{\\textsc{Dominica " + num_dim_per_annum + \
    #         " per annum}}" + " (" + text_ap_pentec + ")"
    # else:
    sainte_reine["header"] = "þ \\textbf{\\MakeUppercase{S. Reginæ, virginis et martyris}} () - \\textbf{sollemnitas minor} - \\textit{Rub.}"
    sainte_reine[
        "body"] = "\n\\item In Officio: omnia de Communi virginum; oratio in supplemento 168.\n\\item Ad Vigilias: hymnus proprius et lectiones II Nocturni in folio supplemento; lectio I Nocturni de libro Ecclesiastici \\textbf{51}, 1-17 in breviario monastico 172*.\n\\item Ad Laudes: versiculum in AM 1178.\n\\item \\textit{In ML: dicitur \\emph{Credo}; præfatio de sanctis martyribus.}\n\\item In MC: collecta propria; Commune virginis martyris (MR 924); lectiones propriæ: Ct \\textbf{8}, 6-7 / Ep \\textbf{6}, 10-13. 18 / Mt \\textbf{25}, 1-13 ; præfatio de sanctis martyribus."
    sainte_reine["II_vesp"] = "\n\\item Vesperæ sollemnitatis. ¶ \\textit{Adiuvabit eam} et versiculum in AM 1178." if sainte_reine_date.weekday(
    ) == 5 else "\\item Ad Vesperas, ¶ \\textit{Adiuvabit eam} et versiculum in AM 1178."
    # Si 1er vendredi du mois, reporter le jeûne au lendemain:
    if sainte_reine_date.weekday() == 4:
        dict_tempo[sainte_reine_date]["symbols"] = dict_tempo[sainte_reine_date]["symbols"].replace(
            " µ", " ł")

    saint_seine_date = datetime.date(current_year, 9, 19)
    saint_seine = dict_flav[saint_seine_date] = {}
    saint_seine["force"] = 40
    saint_seine["header"] = "S. Sequani, abbatis - memoria minor - \\textit{Vir.}"
    if is_third_week_of_september(saint_seine_date):
        if saint_seine_date.weekday() in [2, 4]:
            messe_lue = "\n\\item \\textit{In ML (Viol.): Quatuor Temporum Septembris.}"
        elif saint_seine_date.weekday() == 5:
            messe_lue = "\n\\item \\textit{In ML (Viol.): Quatuor Temporum Septembris (forma Missæ brevior).}"
        else:
            messe_lue = "\n\\item \\textit{In ML (Alb.): Missa pro abbate.}"
    else:
        messe_lue = "\n\\item \\textit{In ML (Alb.): Missa pro abbate.}"
    saint_seine["body"] = "\n\\item Ad Benedictus: ø \\textit{Serve bone} (AM 673); oratio in supplemento 172." + \
        messe_lue + \
        "\n\\item In MC \\textit{(Alb.)}: collecta propria; Commune sanctorum et sanctarum (MR 958)."

    saint_benigne_date = datetime.date(current_year, 11, 13)
    saint_benigne = dict_flav[saint_benigne_date] = {}
    saint_benigne["force"] = 70
    # saint_benigne["anniv"] = "\\textup{†} Cras recurrit anniversarium obitus R. P. Lini Mariæ \\textsc{Delbos}, sacerdotis, qui die 13 novembris 2011, in Abbatia Dominæ Nostræ Mayliliensis, obdormivit in Domino."
    saint_benigne["header"] = "\\textbf{\\textsc{S. Benigni, martyris}} - \\textbf{festum} - \\textit{Rub.}"
    # Si 11/11 et 13/11 appartiennent à la même semaine, on inverse la semaine du psautier pour les Vigiles:
    inv_sem_vigiles = "; antiphonæ et psalmi anni " + \
        hebdo_psalterii_inv[even_year]
    saint_benigne["body"] = "\n\\item In Officio: omnia de Communi unius martyris; oratio in supplemento 188.\n\\item Ad Vigilias: invitatorium proprium in supplemento 59; hymnus in supplemento 185" + inv_sem_vigiles + \
        "; lectiones I et II Nocturnorum in supplemento 185*.\n\\item \\textit{In ML: Missa et præfatio propriæ (olim die 20 novembris; non dicitur \\emph{Credo}).}\n\\item In MC: oratio propria; Commune martyrum (MR 915); lectiones propriæ: 1 Thes \\textbf{2}, 2-8 / Mc \\textbf{16}, 15-18; præfatio de sanctis martyribus."

    sainte_catherine_laboure_date = datetime.date(current_year, 11, 25)
    sainte_catherine_laboure = dict_flav[sainte_catherine_laboure_date] = {}
    sainte_catherine_laboure["force"] = 40
    sainte_catherine_laboure[
        "header"] = "S. Catharinæ Labouré, virginis - memoria minor - \\textit{Vir.}"
    sainte_catherine_laboure["body"] = "\n\\item Ad Benedictus: ø \\textit{Veni sponsa} (AM 678); oratio in supplemento 192.\n\\item \\textit{In ML (Alb.): Missa pro virgine tantum.}\n\\item In MC \\textit{(Alb.)}: collecta propria; Commune virginum (MR 950)."


    return dict_flav