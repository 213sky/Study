# react编程
## 1 项目创建
### 1.1 环境初始化
```
1 安装脚手架服务
    npm install -g create-react-app
2 查看全局安装目录
    npm root -g
```
### 1.2 项目创建
```
1 执行命令
    create-react-app demo_react 
2 运行
    npm install
    npm start
```
### 1.3 组件基本语法

1. 组件(app.js)

```react
import React, {Compent} from 'react'

export default class App extends Compent {
    render(){
        return (
        <div >

        </div>
        )
    }
}
```

2. 入口文件(index.js)

```react
import React from 'react'
import ReactDOM from 'react-dom'
import App from './components/app'  //此处不能写成components/app

ReactDOM.render(<App />, document.getElementById('root'))
```

## 2 React注意事项

### 2.1 HTML标签树形需要转义

| 标签属性名            | React                     |
| --------------------- | ------------------------- |
| class                 | className                 |
| style='display: none' | style={{display: 'none'}} |
|                       |                           |



## 3 项目实践

### 3.1 项目一(评论)
#### 3.1.1 项目效果预览
<img src="./react/评论.png" />
#### 3.1.2 项目开发
##### 3.1.2.1 组件开发



