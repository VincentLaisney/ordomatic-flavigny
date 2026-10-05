# coding: utf-8

import datetime


def dict_solign_create(current_year, even_year, dict_tempo):
    dict_solign = {}

    saint_eloi_date = datetime.date(current_year - 1, 12, 1)
    saint_eloi = dict_solign[saint_eloi_date] = {}
    saint_eloi["force"] = 70
    saint_eloi["header"] = "\\textbf{\\textsc{S. Eligii, episcopi}} - \\textbf{Festum} - \\textit{Alb.}"
    saint_eloi["body"] = "\n\\item In Officio~: oratio in supplemento.\n\\item Ad Vigilias: omnia de communi confessoris pontificis, præter lectio II Nocturni in supplemento.\n\\item In MC~: commune pastorum (MR 938)~; lectiones propriæ~: 1 Cor \\textbf{3}, 9b-11, 16-17 / Mt \\textbf{9}, 35-38~; præfatio de sanctis pastoribus."

    saint_theau_date = datetime.date(current_year, 1, 7)
    saint_theau = dict_solign[saint_theau_date] = {}
    saint_theau["force"] = 20
    saint_theau["header"] = "S. Tillonis, sacerdotis et eremitæ - \\textit{memoria minor} - \\textit{Vir.}"
    saint_theau["body"] = "\n\\item Ad Benedictus: ø \\textit{Serve bone} (AM 673); oratio \\textit{Adesto Domine} de communi confessoris non pontificis.\n\\item \\textit{In ML (Alb.): Missa \\emph{Iustus ut palma} N.2 de communi confessoris non pontificis.}\n\\item In MC: commune sanctorum et sanctarum (MR 959)."

    dedicace_solignac_date = datetime.date(current_year, 5, 8)
    dedicace_solignac = dict_solign[dedicace_solignac_date] = {}
    dedicace_solignac["force"] = 110
    dedicace_solignac["I_vesp"] = "\n\\item I Vesperæ sollemnitatis sequentis."
    dedicace_solignac["header"] = "\\textbf{\\MakeUppercase{In Dedicatione Basilicæ Solignacensis} - sollemnitas minor} - \\textit{Alb.}"
    dedicace_solignac["body"] = "\n\\item Omnia de Communi Dedicationis." 
    dedicace_solignac["body"] += "\n\\item \\textit{In ML: Credo. Præfatio in dedicatione ecclesiæ.}\n\\item In MC: Missa in ipsa ecclesia dedicata. Lectiones propriae~: Ap \\textbf{21}, 1-5a / 1 Cor \\textbf{3}, 9c-11.16-17 / Lc \\textbf{19}, 1-10, \\textit{Credo}, præfatio in dedicatione ecclesiæ."
    
    saint_martial_date = datetime.date(current_year, 6, 30)
    saint_martial = dict_solign[saint_martial_date] = {}
    saint_martial["force"] = 70
    saint_martial["header"] = "\\textbf{\\textsc{S. Martialis, episcopi}} - \\textbf{festum} - \\textit{Alb.}"
    saint_martial["body"] = "\n\\item Omnia de communi confessoris pontificis.\n\\item Ad Vigilias: invitatorium, hymnus et lectiones propriæ (cf. folium).\n\\item \\textit{In ML (Alb.): Missa pro confessore pontifici.}\n\\item In MC~: Orationes in Missale Romano «~pro uno fundatore Ecclesiae~» (MR 935) Præfatio de sanctis pastoribus. Lectiones propriæ~: 2 Tim \\textbf{4}, 1-5 / Io \\textbf{17}, 1-11a"

    dedicace_cathedrale_limoges_date = datetime.date(current_year, 9, 1)
    dedicace_cathedrale_limoges = dict_solign[dedicace_cathedrale_limoges_date] = {}
    dedicace_cathedrale_limoges["force"] = 70
    dedicace_cathedrale_limoges["header"] = "\\textbf{\\textsc{In Dedicatione Basilicæ Cathedralis Limogensis}} - \\textbf{festum} - \\textit{Alb.}"
    dedicace_cathedrale_limoges["body"] = "\n\\item Omnia de Communi dedicationis ecclesiæ.\n\\item Ad Vigilias: lectiones III nocturni."
    dedicace_cathedrale_limoges["body"] += "\n\\item \\textit{In ML: præfatio in dedicatione ecclesiæ (Gloria, Credo).}\n\\item In MC~: Missa de Communi dedicationis ecclesiæ (MR 895)~; Lectiones propriæ~: Ap \\textbf{21}, 1-5a / Io \\textbf{2}, 13-22~; præfatio in dedicatione ecclesiæ II." 

    saint_remacle_date = datetime.date(current_year, 9, 4)
    saint_remacle = dict_solign[saint_remacle_date] = {}
    saint_remacle["force"] = 20
    saint_remacle["header"] = "S. Remaculi, primi abbatis solignacensis - \\textit{memoria minor} - \\textit{Vir.}"
    saint_remacle["body"] = "\n\\item Oratio propria.\n\\item \\textit{In ML (Alb.): Missa pro abbate.}\n\\item In MC \\textit{(Alb.)}"

    sainte_reine_date = datetime.date(current_year, 9, 7)
    sainte_reine = dict_solign[sainte_reine_date] = {}
    sainte_reine["force"] = 40
    sainte_reine["header"] = "S. Reginæ, virginis - memoria minor - \\textit{Vir.}"
    sainte_reine["body"] = "\n\\item Ad Benedictus: ø \\textit{Dilectæ animam} (AM 1136); oratio in supplemento 168."

    sainte_catherine_d_alexandrie_date = datetime.date(current_year, 11, 25)
    sainte_catherine_d_alexandrie = dict_solign[sainte_catherine_d_alexandrie_date] = {}
    sainte_catherine_d_alexandrie["force"] = 20
    sainte_catherine_d_alexandrie[
        "header"] = "S. Catharinæ Alexandriæ, virginis et martyris - \\textit{memoria minor} - \\textit{Vir.}"
    sainte_catherine_d_alexandrie["body"] = "\n\\item Ad Benedictus: ø \\textit{Simile est} et ß \\textit{Diffusa est} (AM 680).\n\\item \\textit{In ML (Rub.)}\n\\item In MC \\textit{(Rub.)}: Commune virginis martyris (MR 924)."   

    return dict_solign