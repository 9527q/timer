#! python
"""
任务计时

空 -> 查看全部任务
任务名 -> 新建/查看任务
clr [任务名] -> 清除某个任务或清空所有任务
"""
import datetime


def time2s(time_or_delta):
    return str(time_or_delta)[:-7]


class Timer:
    def __init__(self):
        self.tasks = {}

    def show_all(self):
        if not self.tasks:
            print('❗️ 暂无在册任务')
            return

        print('🍺 全部任务：')
        now = datetime.datetime.now()
        for name, start in self.tasks.items():
            print(f'\t{name}\t{time2s(start)}\t{time2s(now - start)}')

    def create_or_show(self, name):
        if name in self.tasks:
            start = self.tasks[name]
            print(
                '🍺 任务详情：\n'
                f'\t名称：{name}\n'
                f'\t开始：{start}\n'
                f'\t耗时：{time2s(datetime.datetime.now() - start)}'
            )
        else:
            now = datetime.datetime.now()
            self.tasks[name] = now
            print(f'🍺 添加成功：{name}\t开始时间：{time2s(now)}')

    def clr(self, name=None):
        if not name:
            self.tasks.clear()
            print('🍺 所有任务已清除')
            return

        if name in self.tasks:
            del self.tasks[name]
            print(f'🍺 删除成功：{name}')
        else:
            print(f'❗️ 不存在的任务名：{name}')


if __name__ == '__main__':
    t = Timer()
    while 1:
        try:
            s_in = input('>>> ').strip()
        except (KeyboardInterrupt, EOFError):
            exit(print('\n🍻'))

        if not s_in:
            t.show_all()
        elif s_in.startswith('clr'):
            t.clr((s_in + ' ').split(' ', 1)[1].strip())
        else:
            t.create_or_show(s_in)
