import json
import os
import random
import datetime
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.checkbox import CheckBox
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout

Window.size = (400, 700)

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "students.json")

COLORS = {
    "bg": "#F8FAFC",
    "card": "#FFFFFF",
    "border": "#E2E8F0",
    "primary": "#4F46E5",
    "success": "#10B981",
    "warning": "#F59E0B",
    "danger": "#EF4444",
    "purple": "#8B5CF6",
    "title": "#1E293B",
    "text": "#475569",
    "sub": "#94A3B8",
    "light": "#F1F5F9",
    "select_bg": "#EEF2FF",
    "highlight": "#DC2626",
}

class ColoredBoxLayout(BoxLayout):
    def __init__(self, color=COLORS["bg"], **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(*self.hex_to_rgb(color))
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)
    
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
    
    @staticmethod
    def hex_to_rgb(hex_color):
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16)/255.0 for i in (0, 2, 4)) + (1,)

class CustomButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_color = (0, 0, 0, 0)
        self.color = (1, 1, 1, 1)
        self.font_name = 'DroidSansFallback'
        with self.canvas.before:
            self.bg_color = Color(*ColoredBoxLayout.hex_to_rgb(kwargs.get('bg_color', COLORS["primary"])))
            self.rect = Rectangle(size=self.size, pos=self.pos, radius=[10])
        self.bind(size=self._update_rect, pos=self._update_rect)
    
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

class StudentScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.students = []
        self.selected_indices = set()
        self.load_students()
        self.build_ui()
    
    def load_students(self):
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r", encoding="utf-8") as file:
                    data = json.load(file)
                students_data = data.get("students", [])
                if students_data and isinstance(students_data[0], str):
                    self.students = []
                    for i, name in enumerate(students_data):
                        code = f"{i+1:05d}"
                        self.students.append({"name": name, "code": code})
                else:
                    self.students = students_data
            except:
                self.students = []
        else:
            self.students = []
    
    def save_students(self):
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r", encoding="utf-8") as file:
                    data = json.load(file)
            except:
                data = {}
        else:
            data = {}
        data["students"] = self.students
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
    
    def build_ui(self):
        layout = ColoredBoxLayout(orientation="vertical", color=COLORS["bg"], padding=10, spacing=10)
        
        title = Label(text="学生名单", font_size=24, bold=True, color=ColoredBoxLayout.hex_to_rgb(COLORS["title"]), size_hint_y=None, height=50)
        layout.add_widget(title)
        
        count_label = Label(text=f"{len(self.students)} 人", font_size=14, color=ColoredBoxLayout.hex_to_rgb(COLORS["sub"]), size_hint_y=None, height=30)
        self.count_label = count_label
        layout.add_widget(count_label)
        
        input_layout = BoxLayout(orientation="horizontal", spacing=10, size_hint_y=None, height=50)
        self.name_input = TextInput(hint_text="姓名", size_hint_x=0.5, multiline=False)
        self.code_input = TextInput(hint_text="编码", size_hint_x=0.3, multiline=False)
        add_btn = Button(text="添加", size_hint_x=0.2, background_color=ColoredBoxLayout.hex_to_rgb(COLORS["success"]))
        add_btn.bind(on_press=self.add_student)
        input_layout.add_widget(self.name_input)
        input_layout.add_widget(self.code_input)
        input_layout.add_widget(add_btn)
        layout.add_widget(input_layout)
        
        btn_layout = BoxLayout(orientation="horizontal", spacing=10, size_hint_y=None, height=45)
        delete_btn = Button(text="删除选中", background_color=ColoredBoxLayout.hex_to_rgb(COLORS["danger"]))
        delete_btn.bind(on_press=self.delete_students)
        clear_btn = Button(text="清空", background_color=ColoredBoxLayout.hex_to_rgb(COLORS["warning"]))
        clear_btn.bind(on_press=self.clear_all)
        btn_layout.add_widget(delete_btn)
        btn_layout.add_widget(clear_btn)
        layout.add_widget(btn_layout)
        
        scroll = ScrollView()
        self.student_list_layout = GridLayout(cols=1, spacing=5, size_hint_y=None)
        self.student_list_layout.bind(minimum_height=self.student_list_layout.setter('height'))
        scroll.add_widget(self.student_list_layout)
        layout.add_widget(scroll)
        
        nav_layout = BoxLayout(orientation="horizontal", spacing=10, size_hint_y=None, height=60, padding=[10, 5])
        for screen_name, color in [("点名", COLORS["primary"]), ("签到", COLORS["success"]), ("历史", COLORS["purple"])]:
            btn = Button(text=screen_name, background_color=ColoredBoxLayout.hex_to_rgb(color))
            btn.bind(on_press=lambda x, s=screen_name: self.go_to_screen(s))
            nav_layout.add_widget(btn)
        layout.add_widget(nav_layout)
        
        self.add_widget(layout)
        self.update_list()
    
    def update_list(self):
        self.student_list_layout.clear_widgets()
        self.selected_indices.clear()
        for i, student in enumerate(self.students):
            item_layout = BoxLayout(orientation="horizontal", size_hint_y=None, height=50, padding=[5, 0])
            check = CheckBox(size_hint_x=0.1)
            check.bind(active=lambda x, y, idx=i: self.toggle_select(idx, y))
            label = Label(text=f"{student['name']} ({student['code']})", color=ColoredBoxLayout.hex_to_rgb(COLORS["text"]), size_hint_x=0.9, halign="left")
            label.bind(size=label.setter('text_size'))
            item_layout.add_widget(check)
            item_layout.add_widget(label)
            self.student_list_layout.add_widget(item_layout)
        self.count_label.text = f"{len(self.students)} 人"
    
    def toggle_select(self, index, active):
        if active:
            self.selected_indices.add(index)
        else:
            self.selected_indices.discard(index)
    
    def add_student(self, instance):
        name = self.name_input.text.strip()
        code = self.code_input.text.strip()
        
        if not name:
            self.show_popup("提示", "请输入学生姓名！")
            return
        
        for student in self.students:
            if student["name"] == name:
                self.show_popup("提示", f"学生 \"{name}\" 已存在！")
                return
        
        if code:
            if not code.isdigit() or len(code) != 5:
                self.show_popup("提示", "编码必须是五位数字！")
                return
            for student in self.students:
                if student["code"] == code:
                    self.show_popup("提示", f"编码 \"{code}\" 已存在！")
                    return
        else:
            if self.students:
                max_code = max(int(student["code"]) for student in self.students)
                code = f"{max_code + 1:05d}"
            else:
                code = "00001"
        
        self.students.append({"name": name, "code": code})
        self.save_students()
        self.name_input.text = ""
        self.code_input.text = ""
        self.update_list()
    
    def delete_students(self, instance):
        if not self.selected_indices:
            self.show_popup("提示", "请先选中要删除的学生！")
            return
        
        to_delete = sorted(self.selected_indices, reverse=True)
        for idx in to_delete:
            self.students.pop(idx)
        
        self.save_students()
        self.update_list()
    
    def clear_all(self, instance):
        if not self.students:
            return
        
        def confirm_clear(instance):
            self.students.clear()
            self.save_students()
            self.update_list()
            popup.dismiss()
        
        content = BoxLayout(orientation="vertical", spacing=10, padding=10)
        content.add_widget(Label(text="确定清空所有学生？", color=(0,0,0,1)))
        btn_layout = BoxLayout(orientation="horizontal", spacing=10, size_hint_y=None, height=50)
        yes_btn = Button(text="确定", background_color=ColoredBoxLayout.hex_to_rgb(COLORS["danger"]))
        no_btn = Button(text="取消", background_color=ColoredBoxLayout.hex_to_rgb("#94A3B8"))
        btn_layout.add_widget(no_btn)
        btn_layout.add_widget(yes_btn)
        content.add_widget(btn_layout)
        
        popup = Popup(title="确认", content=content, size_hint=(0.8, 0.3))
        yes_btn.bind(on_press=confirm_clear)
        no_btn.bind(on_press=popup.dismiss)
        popup.open()
    
    def show_popup(self, title, message):
        content = BoxLayout(orientation="vertical", spacing=10, padding=10)
        content.add_widget(Label(text=message, color=(0,0,0,1)))
        btn = Button(text="确定", size_hint_y=None, height=50, background_color=ColoredBoxLayout.hex_to_rgb(COLORS["primary"]))
        content.add_widget(btn)
        
        popup = Popup(title=title, content=content, size_hint=(0.8, 0.3))
        btn.bind(on_press=popup.dismiss)
        popup.open()
    
    def go_to_screen(self, screen_name):
        if screen_name == "点名":
            self.manager.current = "rollcall"
        elif screen_name == "签到":
            self.manager.current = "attendance"
        elif screen_name == "历史":
            self.manager.current = "history"

class RollCallScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.students = []
        self.current_index = 0
        self.is_animating = False
        self.load_data()
        self.build_ui()
    
    def load_data(self):
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r", encoding="utf-8") as file:
                    data = json.load(file)
                self.students = data.get("students", [])
                self.current_index = data.get("current_index", 0)
            except:
                self.students = []
                self.current_index = 0
        else:
            self.students = []
            self.current_index = 0
    
    def save_data(self):
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r", encoding="utf-8") as file:
                    data = json.load(file)
            except:
                data = {}
        else:
            data = {}
        data["current_index"] = self.current_index
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
    
    def on_pre_enter(self):
        self.load_data()
        self.count_label.text = f"共 {len(self.students)} 人"
    
    def build_ui(self):
        layout = ColoredBoxLayout(orientation="vertical", color=COLORS["bg"], padding=10, spacing=10)
        
        title = Label(text="随机点名", font_size=24, bold=True, color=ColoredBoxLayout.hex_to_rgb(COLORS["title"]), size_hint_y=None, height=50)
        layout.add_widget(title)
        
        self.count_label = Label(text=f"共 {len(self.students)} 人", font_size=14, color=ColoredBoxLayout.hex_to_rgb(COLORS["sub"]), size_hint_y=None, height=30)
        layout.add_widget(self.count_label)
        
        num_layout = BoxLayout(orientation="horizontal", spacing=10, size_hint_y=None, height=50)
        num_layout.add_widget(Label(text="点名人数:", color=ColoredBoxLayout.hex_to_rgb(COLORS["text"]), size_hint_x=0.4))
        self.num_input = TextInput(text="1", multiline=False, size_hint_x=0.2)
        num_layout.add_widget(self.num_input)
        for n in [1, 2, 3, 5]:
            btn = Button(text=str(n), size_hint_x=0.1, background_color=ColoredBoxLayout.hex_to_rgb(COLORS["select_bg"]), color=ColoredBoxLayout.hex_to_rgb(COLORS["primary"]))
            btn.bind(on_press=lambda x, val=n: self.set_num(val))
            num_layout.add_widget(btn)
        layout.add_widget(num_layout)
        
        result_card = ColoredBoxLayout(color=COLORS["light"], padding=20, spacing=10)
        self.result_label = Label(text="等待点名...", font_size=32, bold=True, color=ColoredBoxLayout.hex_to_rgb(COLORS["sub"]))
        result_card.add_widget(self.result_label)
        layout.add_widget(result_card)
        
        self.progress_label = Label(text="", font_size=14, color=ColoredBoxLayout.hex_to_rgb(COLORS["sub"]), size_hint_y=None, height=30)
        layout.add_widget(self.progress_label)
        
        btn_layout = BoxLayout(orientation="horizontal", spacing=10, size_hint_y=None, height=60)
        random_btn = Button(text="随机点名", background_color=ColoredBoxLayout.hex_to_rgb(COLORS["primary"]), font_size=18)
        random_btn.bind(on_press=self.random_roll_call)
        seq_btn = Button(text="顺序点名", background_color=ColoredBoxLayout.hex_to_rgb(COLORS["warning"]), font_size=18)
        seq_btn.bind(on_press=self.sequential_roll_call)
        btn_layout.add_widget(random_btn)
        btn_layout.add_widget(seq_btn)
        layout.add_widget(btn_layout)
        
        nav_layout = BoxLayout(orientation="horizontal", spacing=10, size_hint_y=None, height=60, padding=[10, 5])
        for screen_name, color in [("学生", COLORS["purple"]), ("签到", COLORS["success"]), ("历史", COLORS["purple"])]:
            btn = Button(text=screen_name, background_color=ColoredBoxLayout.hex_to_rgb(color))
            btn.bind(on_press=lambda x, s=screen_name: self.go_to_screen(s))
            nav_layout.add_widget(btn)
        layout.add_widget(nav_layout)
        
        self.add_widget(layout)
    
    def set_num(self, value):
        self.num_input.text = str(value)
    
    def get_num(self):
        try:
            n = int(self.num_input.text.strip())
            return max(1, n)
        except ValueError:
            return 1
    
    def random_roll_call(self, instance):
        if not self.students:
            self.show_popup("提示", "名单为空，请先添加学生！")
            return
        if self.is_animating:
            return
        
        num = self.get_num()
        if num > len(self.students):
            self.show_popup("提示", f"点名人数({num})超过学生总数({len(self.students)})！")
            return
        
        self.is_animating = True
        self.targets = random.sample(self.students, num)
        self.animation_step = 0
        self.total_steps = 22
        Clock.schedule_interval(self.animate, 0.05)
    
    def animate(self, dt):
        self.animation_step += 1
        if self.animation_step < self.total_steps:
            sample = random.sample(self.students, min(self.get_num(), len(self.students)))
            display = "、".join([s["name"] for s in sample])
            self.result_label.text = display
            self.result_label.color = ColoredBoxLayout.hex_to_rgb(COLORS["primary"])
        else:
            display = "、".join([s["name"] for s in self.targets])
            self.result_label.text = display
            self.result_label.color = ColoredBoxLayout.hex_to_rgb(COLORS["highlight"])
            self.progress_label.text = f"随机点名完成 (共 {len(self.targets)} 人)"
            self.is_animating = False
            return False
    
    def sequential_roll_call(self, instance):
        if not self.students:
            self.show_popup("提示", "名单为空，请先添加学生！")
            return
        if self.is_animating:
            return
        
        num = self.get_num()
        if num > len(self.students):
            self.show_popup("提示", f"点名人数({num})超过学生总数({len(self.students)})！")
            return
        
        if self.current_index >= len(self.students):
            self.current_index = 0
        
        names = []
        for _ in range(num):
            if self.current_index >= len(self.students):
                self.current_index = 0
            names.append(self.students[self.current_index]["name"])
            self.current_index += 1
        
        if self.current_index >= len(self.students):
            self.current_index = 0
        
        display = "、".join(names)
        self.result_label.text = display
        self.result_label.color = ColoredBoxLayout.hex_to_rgb(COLORS["highlight"])
        end_idx = self.current_index if self.current_index > 0 else len(self.students)
        self.progress_label.text = f"顺序点名  已点到第 {end_idx} / {len(self.students)} 人"
        self.save_data()
    
    def show_popup(self, title, message):
        content = BoxLayout(orientation="vertical", spacing=10, padding=10)
        content.add_widget(Label(text=message, color=(0,0,0,1)))
        btn = Button(text="确定", size_hint_y=None, height=50, background_color=ColoredBoxLayout.hex_to_rgb(COLORS["primary"]))
        content.add_widget(btn)
        
        popup = Popup(title=title, content=content, size_hint=(0.8, 0.3))
        btn.bind(on_press=popup.dismiss)
        popup.open()
    
    def go_to_screen(self, screen_name):
        if screen_name == "学生":
            self.manager.current = "student"
        elif screen_name == "签到":
            self.manager.current = "attendance"
        elif screen_name == "历史":
            self.manager.current = "history"

class AttendanceScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.students = []
        self.attendance_records = {}
        self.today = datetime.date.today().strftime("%Y-%m-%d")
        self.attended_students = []
        self.load_data()
        self.build_ui()
    
    def load_data(self):
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r", encoding="utf-8") as file:
                    data = json.load(file)
                self.students = data.get("students", [])
                self.attendance_records = data.get("attendance", {})
                
                for date, students in self.attendance_records.items():
                    if students and isinstance(students[0], str):
                        new_students = []
                        for name in students:
                            for s in self.students:
                                if s["name"] == name:
                                    new_students.append(s)
                                    break
                        self.attendance_records[date] = new_students
            except:
                self.students = []
                self.attendance_records = {}
        else:
            self.students = []
            self.attendance_records = {}
        
        self.attended_students = list(self.attendance_records.get(self.today, []))
    
    def save_data(self):
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r", encoding="utf-8") as file:
                    data = json.load(file)
            except:
                data = {}
        else:
            data = {}
        data["attendance"] = self.attendance_records
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
    
    def on_pre_enter(self):
        self.today = datetime.date.today().strftime("%Y-%m-%d")
        self.load_data()
        self.update_stats()
        self.update_list()
    
    def build_ui(self):
        layout = ColoredBoxLayout(orientation="vertical", color=COLORS["bg"], padding=10, spacing=10)
        
        title = Label(text=f"学生签到 - {self.today}", font_size=20, bold=True, color=ColoredBoxLayout.hex_to_rgb(COLORS["title"]), size_hint_y=None, height=50)
        layout.add_widget(title)
        
        self.status_label = Label(text="", font_size=14, size_hint_y=None, height=30)
        layout.add_widget(self.status_label)
        
        stats_layout = BoxLayout(orientation="horizontal", spacing=10, size_hint_y=None, height=40)
        self.attended_label = Label(text="已签到: 0", color=ColoredBoxLayout.hex_to_rgb(COLORS["success"]), bold=True)
        self.not_attended_label = Label(text=f"未签到: {len(self.students)}", color=ColoredBoxLayout.hex_to_rgb(COLORS["danger"]), bold=True)
        self.total_label = Label(text=f"总人数: {len(self.students)}", color=ColoredBoxLayout.hex_to_rgb(COLORS["text"]))
        stats_layout.add_widget(self.attended_label)
        stats_layout.add_widget(self.not_attended_label)
        stats_layout.add_widget(self.total_label)
        layout.add_widget(stats_layout)
        
        input_layout = BoxLayout(orientation="horizontal", spacing=10, size_hint_y=None, height=50)
        self.code_input = TextInput(hint_text="请输入编码（逗号分隔批量）", multiline=False)
        check_btn = Button(text="签到", size_hint_x=0.3, background_color=ColoredBoxLayout.hex_to_rgb(COLORS["success"]))
        check_btn.bind(on_press=self.check_code)
        input_layout.add_widget(self.code_input)
        input_layout.add_widget(check_btn)
        layout.add_widget(input_layout)
        
        list_title = Label(text="已签到学生", font_size=16, bold=True, color=ColoredBoxLayout.hex_to_rgb(COLORS["title"]), size_hint_y=None, height=30)
        layout.add_widget(list_title)
        
        scroll = ScrollView()
        self.attended_list_layout = GridLayout(cols=1, spacing=5, size_hint_y=None)
        self.attended_list_layout.bind(minimum_height=self.attended_list_layout.setter('height'))
        scroll.add_widget(self.attended_list_layout)
        layout.add_widget(scroll)
        
        finish_btn = Button(text="完成签到", size_hint_y=None, height=55, background_color=ColoredBoxLayout.hex_to_rgb(COLORS["primary"]), font_size=18)
        finish_btn.bind(on_press=self.finish_attendance)
        layout.add_widget(finish_btn)
        
        nav_layout = BoxLayout(orientation="horizontal", spacing=10, size_hint_y=None, height=60, padding=[10, 5])
        for screen_name, color in [("学生", COLORS["purple"]), ("点名", COLORS["primary"]), ("历史", COLORS["purple"])]:
            btn = Button(text=screen_name, background_color=ColoredBoxLayout.hex_to_rgb(color))
            btn.bind(on_press=lambda x, s=screen_name: self.go_to_screen(s))
            nav_layout.add_widget(btn)
        layout.add_widget(nav_layout)
        
        self.add_widget(layout)
        self.update_stats()
        self.update_list()
    
    def update_stats(self):
        attended_count = len(self.attended_students)
        not_attended_count = len(self.students) - attended_count
        self.attended_label.text = f"已签到: {attended_count}"
        self.not_attended_label.text = f"未签到: {not_attended_count}"
        self.total_label.text = f"总人数: {len(self.students)}"
    
    def update_list(self):
        self.attended_list_layout.clear_widgets()
        for i, student in enumerate(self.attended_students):
            label = Label(text=f"{i+1}. {student['name']} ({student['code']})", 
                         color=ColoredBoxLayout.hex_to_rgb(COLORS["text"]), 
                         size_hint_y=None, height=40, halign="left")
            label.bind(size=label.setter('text_size'))
            self.attended_list_layout.add_widget(label)
    
    def check_code(self, instance):
        code_input = self.code_input.text.strip()
        
        if not code_input:
            self.status_label.text = "请输入编码！"
            self.status_label.color = ColoredBoxLayout.hex_to_rgb(COLORS["danger"])
            return
        
        codes = [code.strip() for code in code_input.split(",")]
        success_count = 0
        error_messages = []
        successful_students = []
        
        for code in codes:
            if not code:
                continue
            
            if not code.isdigit() or len(code) != 5:
                error_messages.append(f"编码 {code} 必须是五位数字")
                continue
            
            student = None
            for s in self.students:
                if s["code"] == code:
                    student = s
                    break
            
            if not student:
                error_messages.append(f"编码 {code} 不存在")
                continue
            
            already_attended = False
            for s in self.attended_students:
                if s["code"] == code:
                    error_messages.append(f"{student['name']} 已签到")
                    already_attended = True
                    break
            
            if already_attended:
                continue
            
            self.attended_students.append(student)
            successful_students.append(student)
            success_count += 1
        
        if success_count > 0:
            if success_count == 1:
                student_name = successful_students[0]["name"]
                self.status_label.text = f"{student_name} 签到成功！"
            else:
                self.status_label.text = f"成功签到 {success_count} 名学生！"
            self.status_label.color = ColoredBoxLayout.hex_to_rgb(COLORS["success"])
            self.update_stats()
            self.update_list()
        
        if error_messages:
            self.status_label.text = "、".join(error_messages)
            self.status_label.color = ColoredBoxLayout.hex_to_rgb(COLORS["danger"])
        
        self.code_input.text = ""
    
    def finish_attendance(self, instance):
        if not self.attended_students:
            self.show_popup("提示", "暂无学生签到！")
            return
        
        self.attendance_records[self.today] = self.attended_students
        self.save_data()
        
        attended_count = len(self.attended_students)
        student_names = [student["name"] for student in self.attended_students]
        self.show_popup("签到成功", f"日期: {self.today}\n签到人数: {attended_count} 人\n签到学生: {', '.join(student_names[:5])}{'...' if len(student_names) > 5 else ''}")
    
    def show_popup(self, title, message):
        content = BoxLayout(orientation="vertical", spacing=10, padding=10)
        content.add_widget(Label(text=message, color=(0,0,0,1)))
        btn = Button(text="确定", size_hint_y=None, height=50, background_color=ColoredBoxLayout.hex_to_rgb(COLORS["primary"]))
        content.add_widget(btn)
        
        popup = Popup(title=title, content=content, size_hint=(0.8, 0.4))
        btn.bind(on_press=popup.dismiss)
        popup.open()
    
    def go_to_screen(self, screen_name):
        if screen_name == "学生":
            self.manager.current = "student"
        elif screen_name == "点名":
            self.manager.current = "rollcall"
        elif screen_name == "历史":
            self.manager.current = "history"

class HistoryScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.attendance_records = {}
        self.students = []
        self.load_data()
        self.build_ui()
    
    def load_data(self):
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r", encoding="utf-8") as file:
                    data = json.load(file)
                self.attendance_records = data.get("attendance", {})
                self.students = data.get("students", [])
            except:
                self.attendance_records = {}
                self.students = []
        else:
            self.attendance_records = {}
            self.students = []
    
    def on_pre_enter(self):
        self.load_data()
        self.update_list()
    
    def build_ui(self):
        layout = ColoredBoxLayout(orientation="vertical", color=COLORS["bg"], padding=10, spacing=10)
        
        title = Label(text="签到历史", font_size=24, bold=True, color=ColoredBoxLayout.hex_to_rgb(COLORS["title"]), size_hint_y=None, height=50)
        layout.add_widget(title)
        
        scroll = ScrollView()
        self.history_list_layout = GridLayout(cols=1, spacing=5, size_hint_y=None)
        self.history_list_layout.bind(minimum_height=self.history_list_layout.setter('height'))
        scroll.add_widget(self.history_list_layout)
        layout.add_widget(scroll)
        
        nav_layout = BoxLayout(orientation="horizontal", spacing=10, size_hint_y=None, height=60, padding=[10, 5])
        for screen_name, color in [("学生", COLORS["purple"]), ("点名", COLORS["primary"]), ("签到", COLORS["success"])]:
            btn = Button(text=screen_name, background_color=ColoredBoxLayout.hex_to_rgb(color))
            btn.bind(on_press=lambda x, s=screen_name: self.go_to_screen(s))
            nav_layout.add_widget(btn)
        layout.add_widget(nav_layout)
        
        self.add_widget(layout)
        self.update_list()
    
    def update_list(self):
        self.history_list_layout.clear_widgets()
        
        if not self.attendance_records:
            label = Label(text="暂无签到记录", color=ColoredBoxLayout.hex_to_rgb(COLORS["sub"]), size_hint_y=None, height=100)
            self.history_list_layout.add_widget(label)
        else:
            sorted_dates = sorted(self.attendance_records.keys(), reverse=True)
            for date in sorted_dates:
                attended_students = self.attendance_records[date]
                attended_count = len(attended_students)
                total_count = len(self.students)
                
                card = ColoredBoxLayout(color=COLORS["card"], orientation="vertical", padding=10, spacing=5, size_hint_y=None, height=120)
                date_label = Label(text=f"📅 {date}", font_size=16, bold=True, color=ColoredBoxLayout.hex_to_rgb(COLORS["primary"]), halign="left")
                date_label.bind(size=date_label.setter('text_size'))
                card.add_widget(date_label)
                
                stats_label = Label(text=f"签到人数: {attended_count}/{total_count}", color=ColoredBoxLayout.hex_to_rgb(COLORS["text"]), halign="left")
                stats_label.bind(size=stats_label.setter('text_size'))
                card.add_widget(stats_label)
                
                if attended_students:
                    student_info = [f"{student['name']}" for student in attended_students]
                    students_label = Label(text=f"学生: {', '.join(student_info[:5])}{'...' if len(student_info) > 5 else ''}", color=ColoredBoxLayout.hex_to_rgb(COLORS["sub"]), font_size=12, halign="left")
                    students_label.bind(size=students_label.setter('text_size'))
                    card.add_widget(students_label)
                
                self.history_list_layout.add_widget(card)
    
    def go_to_screen(self, screen_name):
        if screen_name == "学生":
            self.manager.current = "student"
        elif screen_name == "点名":
            self.manager.current = "rollcall"
        elif screen_name == "签到":
            self.manager.current = "attendance"

class StudentRollCallApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(StudentScreen(name="student"))
        sm.add_widget(RollCallScreen(name="rollcall"))
        sm.add_widget(AttendanceScreen(name="attendance"))
        sm.add_widget(HistoryScreen(name="history"))
        return sm

if __name__ == "__main__":
    StudentRollCallApp().run()
