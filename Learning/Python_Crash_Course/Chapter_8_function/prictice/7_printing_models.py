# 在函数中修改列表

# 无函数版本
""" # 首先创建一个列表，其中包含一些要打印的设计
unprinted_designs = ['iphone case', 'robot pendat', 'dodecahedron']
completed_models = []
# 模拟打印每个设计，知道没有未打印的设计为止
# 打印每个设计后，都将其移到列表 completed_models 中
while unprinted_designs:
    current_design = unprinted_designs.pop()
    # 模拟根据设计制作3D打印模型的过程
    print("Printing model: " + current_design)
    completed_models.append(current_design)
# 显示打印好的所有模型
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model) """

# 函数版本


def print_models(unprinted_designs, completed_models):
    """模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表 completed_models 中

    Args:
        unprinted_designs (list): 未打印的设计列表
        completed_models (list): 完成的模型列表
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # 模拟根据设计制作3D打印模型的过程
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """显示打印好的所有模型

    Args:
        completed_models (list): 打印好的模型列表
    """
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendat', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# 禁止函数修改列表
# print_models(unprinted_designs[:], completed_models)  传递列表副本
