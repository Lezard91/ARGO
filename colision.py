# coding: utf-8

import control_user as ctrl
import map_print as map
import variables as var

TextLine = 0
# check if movement is valid
MapElementAtPlayerPosition = var.map_data[ctrl.player_Y - 1][ctrl.player_X - 1]
MapElementData = var.player_in_map[MapElementAtPlayerPosition]
if MapElementData["CanWalk"]:
    map.print_map(True)
    var.player_data["Y"] = ctrl.player_Y
    var.player_data["X"] = ctrl.player_X
    map.print_map()
    if MapElementAtPlayerPosition == "S":
        var.GameIsRunning = False
        RC.ColorPrintAt(
            "\nBRAVO, tu as trouvé la sortie.",
            Y=var.TextLine+2,
            X=1)
else:
    # obstacle
    print(f"Aïe, un {MapElementData['Name']} !")


