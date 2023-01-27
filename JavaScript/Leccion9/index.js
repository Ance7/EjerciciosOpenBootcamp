const winston = require('winston');

const logger = winston.createLogger({
    level: 'error',
    format: winston.format.json(),
    defaultMeta: { service: 'user-service' },
    transports: [
        new winston.transports.File({ filename: 'error.log', level: 'error' }),
    ],
});

function showError() {
    throw new Error("Error de funcion")
}

try {
    showError()
    } catch (e) {
        logger.log("error", e.toString())
    }


if (process.env.NODE_ENV !== 'production') {
    logger.add(new winston.transports.Console({
    format: winston.format.simple(),
    }));
}