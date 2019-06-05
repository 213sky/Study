# ES6基本语法

## 1 环境搭建
**node.js不直接支持es6语法，需要前期一些准备**
### 1.1 必备包安装
```
1. 全局安装es-checker
	npm install -g es-checker
	查看Node.js对ES6的支持情况
	es-checker 
2. 安装babel-core
	npm install babel-core --save
3. 安装babel-preset-es2015
	npm install babel-preset-es2015
```
### 1.2 项目搭建
```
1. 进入指定目录
2. npm init初始化工作目录
	npm init -y
3. 本地安装Babel-cli(也可以选择全局安装)
	// 本地安装
	npm install babel-cli -g
	// 本地安装
	npm install babel-cli --save
4. 安装babel-preset-es2015来支持ES6的语法
	npm install babel-preset-es2015 --save
5. 创建一个名为.babelrc的配置文件，方便babel-cli使用babel-preset-es2015
	文件创建注意事项，windows不支持".babelrc"直接命名方式，需要采用".babelrc."
	文件内容
	{
		"presets": [
			"es2015"
		],
		"plugins": []
	}
```
### 1.3 测试项目
```
1. 创建测试文件一(app.js)
	export var m = 10
2. 创建测试文件二(test.js)
	import {m} from './app'
	console.log(m)
3. 运行测试
	不能执行运行"node test.js"，否则会报错
	3.1. 当"babel-cli"全局安装，可以直接运行
		babel-node test.js
	3.2. 当"babel-cli"本地安装时
		1) 在package.json文件的scripts添加命令"babel": "babel-node test.js"
		2) 执行"npm run babel"
```


## 2 export

### 2.1 export default详解

#### 2.1.1 基本用法
**使用import命令的时候，用户需要知道所要加载的变量名或函数名，否则无法加载。**但是，用户肯定希望快速上手，未必愿意阅读文档，去了解模块有哪些属性和方法。**为了给用户提供方便，让他们不用阅读文档就能加载模块，就要用到export default命令，为模块指定默认输出。**
```javascript
//export-default.js 这是一个模块文件export-default.js，它的默认输出是一个函数
export default function () {
  console.log('foo');
}
```