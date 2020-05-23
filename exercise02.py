"""
使用进程池完成
假设一个文件夹中有大量的文件，现在需要将这个文件夹备份一份
我们将文件夹中给每个文件的复制作为一个进程池时间对待
提示： os.mkdir() 创建文件夹
思路：   原有文件夹--》新建文件夹
"""
from multiprocessing import Pool
import os
# 复制一个文件
def copy_file(filename,old_folder,new_folder):
    """
    :param filename:要拷贝的文件
    """
    fr=open(old_folder+filename,"rb")
    fw=open(new_folder+filename,"wb")
    while True:
        data=fr.read(1024)
        if not data:
            break
        fw.write(data)
    fr.close()
    fw.close()

# 创建进程池
def main():
    old_folder="  " # 要备份的文件夹
    new_folder="  "
    os.mkdir(new_folder)
    # 加入要执行的事件
    pool=Pool()
    # 加入进程池
    for file in os.listdir(old_folder):
        pool.apply_async(func=copy_file,args=(file,old_folder,new_folder))
    # 关闭进程池，不能加入新的事件
    pool.close()
    # 等待
    pool.join()

if __name__=="__main__":
    main()
