from tkinter import Tk
from tkinter import messagebox
import ttkbootstrap as ttk
from function.DownBoxModify import DownBoxModify
from function.variables.ProjectPathVariables import PRE_DATA, PRE_DATA_PATH


class QuicklyCreate:
    def __init__(self, main_window):
        self.main_window = main_window
        self.main_frame = ttk.Frame(self.main_window)

    def quickly_create_drop_down_box(
        self,
        name_list: list[str],
        overlay_lists: list[list[str]],
        data_json,
        data_json_path: str,
        uniform_width: int = None,
        main_frame_column: int = 0,
        main_frame_row: int = 0,
        input_padx:int=10,
        input_pady:int=10
        ) -> None:
        """
        快速创建多个下拉框并绑定事件。

        参数:
        :param input_pady: 设置pady
        :param input_padx: 设置padx
        :param name_list: 每个下拉框的标签名称。
        :param overlay_lists: 每个下拉框的可选值列表。
        :param data_json: 使用 JsonFile 的对象。
        :param data_json_path: JSON 文件路径。
        :param uniform_width: 所有下拉框的统一宽度，默认为 None。
        :param main_frame_column: 主框架的列位置。
        :param main_frame_row: 主框架的行位置。
        """

        drop_down_box_num = len(name_list)#要创建的下拉框数量

        self.main_frame.grid(row=main_frame_row, column=main_frame_column)

        down_dox_values_group_main = []
        down_dox_group_main = []

        for index in range(drop_down_box_num):
            down_dox_values_group_main.append(overlay_lists[index])

        for i in range(drop_down_box_num):
            text = ttk.Label(self.main_frame, text=name_list[i])
            text.grid(column=0, row=i,padx=10,pady=10)

            drop_down_box = ttk.Combobox(
                self.main_frame,
                values=overlay_lists[i],
                state="readonly",
                width=uniform_width if uniform_width else None,
            )

            down_dox_group_main.append(drop_down_box)

            drop_down_box.bind("<<ComboboxSelected>>", lambda event: DownBoxModify(data_json,
                                                                                   data_json_path,
                                                                                   down_dox_values_group_main,
                                                                                   down_dox_group_main)
                               .for_modify()
                               )

            drop_down_box.grid(column=1, row=i,padx=input_padx,pady=input_pady)

        messagebox.showerror("错误", message=f"{data_json}", parent=window) if isinstance(data_json,
                                                                                                 Exception) else DownBoxModify(
            data_json,
            data_json_path,
            down_dox_values_group_main,
            down_dox_group_main).for_set()


if __name__ == '__main__':
    window = Tk()
    QuicklyCreate(window).quickly_create_drop_down_box(["1","2","3","4","5"],
                                                       [["2","3"],["2","3"],["2","3"],["2","3"],["2","3"]],
                                                       PRE_DATA,PRE_DATA_PATH)
    window.mainloop()