from CopyFromTpp import file_names,Copy

if __name__ =="__main__":
    # 配置
    repo_dir = r"D:\GitProject\tpp311\QYCAM\bin\Debug"          # 源目录（可包含子文件夹）
    source_dir = r"D:\GitProject\tppDLL\Debug"            # 本地仓库目录（将创建）
    Copy(source_dir,  repo_dir )
    repo_dir = r"D:\GitProject\tpp311\QYCAM\bin\Release"  # 源目录（可包含子文件夹）
    source_dir= r"D:\GitProject\tppDLL\Release"  # 本地仓库目录（将创建）
    Copy(source_dir, repo_dir)