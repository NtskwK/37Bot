# 37Bot

基于 [NcatBot](https://github.com/liyihao1110/NcatBot) 的 QQ 机器人。

## 快速开始

### 1. 安装依赖

```bash
uv sync
```

### 2. 配置

复制配置模板并填写：

```bash
cp config.yaml.example config.yaml
```

编辑 `config.yaml`：

```yaml
root: '管理员QQ号'
bt_uin: '机器人QQ号'
napcat:
  ws_uri: ws://localhost:3001      # NapCat WebSocket 地址
  remote_mode: true                 # 远程模式
```

### 3. 运行

```bash
python main.py
```

## 项目结构

```plaintext
37Bot/
├── main.py              # 主程序入口
├── config.yaml          # 配置文件 (git ignored)
├── config.yaml.example  # 配置模板
├── plugins/             # 插件目录
│   ├── status/          # 服务器状态查询
│   ├── help/            # 帮助命令
│   ├── mirrorchyan/     # Mirror酱资源下载
│   ├── groupadmin/      # 群管理
│   └── todo/            # 群待办
├── 37bot.service        # systemd 服务配置
└── start-napcat.sh      # NapCat Docker 启动脚本
```

## 插件功能

### 帮助

- `/help` - 显示模块列表
- `/help <模块>` - 显示模块命令

### 状态

- `/status` - 查询服务器状态（CPU、内存、Swap、磁盘、运行时间）

### Mirror酱

- `/mc_cdk <rid> <cdk>` - 绑定 CDK
- `/mc_download <rid>` - 下载资源
- `/mc_upload <rid>` - 上传资源（回复文件消息）

### 群管

- `/ga_enable` - [管理员] 启用本群群管功能
- `/ga_disable` - [管理员] 禁用本群群管功能
- `/ga_pattern <正则>` - [管理员] 设置入群验证正则
- `/ga_reject <启用> <理由>` - [管理员] 设置自动拒绝
- `/ga_status` - 查看本群群管状态
- `/ga_query [QQ号]` - [管理员] 查询成员记录

### 待办

- `/todo_add <内容>` - 添加待办（支持回复消息）
- `/todo_list` - 查看待办列表
- `/todo_done <id>` - 完成待办

## License

[GPL-3.0](LICENSE)
