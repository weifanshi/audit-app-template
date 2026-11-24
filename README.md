# 审计小程序模板

以后新增审计小程序的统一脚手架，复用 `audit-spec`。

## 必须遵守

- 导入映射：`audit-import-profile`，按工作表 + 表头指纹保存；
- 导出工作簿：隐藏 `__META`，`audit-workbook-manifest`；
- 规则版本与程序版本分离；
- 离线优先，不依赖在线 AI；
- 1024×720 界面验收；
- x86_64/ARM64 双架构打包，附 SHA256。

## 目录

```
src/                 程序源码
tests/               单元测试
docs/验收清单.md     上线前逐项检查
templates/           工作簿模板示例
```

## 快速开始

1. 复制本目录为 `<新程序名>`；
2. 在 `audit-spec` 中补字段和规则；
3. 实现 `import_profile.py`、`export_manifest.py`；
4. 通过验收清单后打包。
