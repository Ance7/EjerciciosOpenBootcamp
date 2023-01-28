import * as controller from './controller.js'
import chalk from 'chalk'

const sum = controller.suma(1, 2)
console.log(sum)

const multi = controller.multiplica(4, 5)
console.log(chalk.green(multi))
