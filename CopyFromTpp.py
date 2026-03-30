
file_names = ["3DProcessInfoModel","BarrelTool","CamTemplateModel"
        ,"DrillOperation","DrillTool","ExportCommonFunc",
        "FixtureElement","GUIModel","LatheOperation",
        "LinePickupV3Model","MachineModel","MillOperation",
        "PostExtend","PyExt","ResourceLibraryModel","ResourceLibraryModelBase",
        "RuleModel","SpecialShapedTool","StdTool","ToolCuttingDataModel",
        "ToolPath","TppCommon","TppMath","TPPModel","TppMwUtils"
        ,"TurningTool","UserDefinedMillTool","UserDefinedOperation",
        "3DProcessInfoBuilder","BarrelToolBuilder","CamTemplateBuilder",
        "CustomFunctionBuilder","DrillOperationBuilder","DrillToolBuilder",
        "FixtureBuilder","FixtureLocatingBuilder","LatheOperationBuilder",
        "LinePickupV3Builder","MachineBuilder","MachineRender",
        "MachineSimulationBuilder","ManufacturabilityCheckBuilder","MillOperationBuilder",
        "OperationBuilder","PartSearchBuilder","PostProcessorBuilder","ResourceLibraryBuilder",
        "ResourceLibraryManager","RMSimulationBuilder","ShortestToolExtensionLengthBuilder"
        ,"SpecialShapedToolBuilder","StdToolBuilder","ToolCuttingDataBuilder",
        "ToolRemovalSimulationBuilder","ToolTypeBuilder","TppApi","TPPBuilder",
        "TppBuilderCommon","TppElementCollection","TPPNavigatorCommon",
        "TurningProfileBuilder","TurningToolBuilder","UserDefinedMillToolBuilder",
        "UserDefinedOperationBuilder","3DProcessInfoUI","BarrelToolUi","CamTemplateUI"
        ,"CustomFunctionUI","DrillOperationUi","DrillToolUi","FixtureLocatingUI",
        "FixtureUI","LatheOperationUi","LinePickupV3Ui","MachineEntityView",
        "MachineSimulationUI","MachineUI","ManufacturabilityCheckUI"
        ,"MillOperationUi","PartSearchUI","ResourceLibraryItemView","ResourceLibraryUI"
        ,"RMSimulationUI","SpecialShapedToolUi","StdToolUi","ToolCuttingDataUI","ToolRemovalSimulationUI"
        ,"TPPBaseUI","TPPCommand","TPPNavigatorView","TPPUI","TppUiCommon",
        "TurningProfileUi","TurningToolUi","UserDefinedMillToolUi","UserDefinedOperationUi","TPPPlugin",
        "TestDialogWith311SelectBlock","TestDynamicUIBuilder","TestDynamicUIDialog"
        ,"TppTestCommand","TppTestPlugin","TestExe"]

import os
import shutil
from pathlib import Path

def Copy(source_dir,repo_dir):
    # 创建仓库目录
    repo_path = Path(repo_dir)
    repo_path.mkdir(parents=True, exist_ok=True)
    # 遍历源目录，复制匹配的文件
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.lower().endswith('.dll'):  # 先筛出 DLL
                # 根据条件判断是否复制
                if file in file_names:  # 精确匹配文件名
                    src = os.path.join(root, file)
                    dst = repo_path / file
                    # 处理重名：如果同名文件已存在，可以重命名或覆盖
                    if dst.exists():
                        os.remove(dst)
                        shutil.copy2(src, dst)
                    else:
                        shutil.copy2(src, dst)
                    print(f"已复制: {file}")
                # 如果用通配符，可改用 fnmatch
                # import fnmatch
                # for pattern in patterns:
                #     if fnmatch.fnmatch(file.lower(), pattern.lower()):
                #         shutil.copy2(src, repo_path / file)
                #         print(f"已复制: {file}")
                #         break

if __name__ =="__main__":
    # 配置
    source_dir = r"D:\GitProject\tpp311\QYCAM\bin\Debug"          # 源目录（可包含子文件夹）
    repo_dir = r"D:\GitProject\tppDLL\Debug"            # 本地仓库目录（将创建）
    Copy(source_dir,  repo_dir )
    # source_dir = r"D:\GitProject\tpp311\QYCAM\bin\Release"  # 源目录（可包含子文件夹）
    # repo_dir = r"D:\GitProject\tppDLL\Release"  # 本地仓库目录（将创建）
    # Copy(source_dir, repo_dir)
