// const prime = () => {
//     console.log(number)
// }


const isprime = (num) => {
    
    // Por default, se considera que es primo, hay que evaluar si no lo es
    let prime = true;

    // El 1 no es primo
    if (num == 1){
        prime = false
    }
    // Esto es para que el 2 no me moleste en la ecuación posterior
    else if(num == 2){
        prime = true
    } 
    // Si es par no es primo
    else if (num % 2 == 0) {
        prime = false
    }
    else {
        for (let i = num - 1; i > 1; i--) {
            // Esto es lo que evalúa si el número es primo o no
            if(num % i == 0){
                prime = false
                break
            } else {
                prime = true
            }
            // Hasta aquí
        }
    }
    return(prime)
}

// Esto es para evaluar una serie de números
for (let i = 1; i < 1000; i++){
    let primo = isprime(i)
    if(primo) {
        console.log(i, `is prime`)
    }
}
