(ns teste.core
  (:gen-class))

(println "Bem vindo ao sistema de estoque!")

(def total-de-produtos 15)
(println total-de-produtos)

(def estoque ["Mochila", "Notebook"])

(estoque 0)
(count estoque)

(conj estoque "Mouse Gamer")
(println estoque)

(def estoque (conj estoque "Mouse Gamer"))
(println estoque)

(defn imprime-mensagem []
  (println "Seja bem vindo(a) ao estoque!"))
(imprime-mensagem)

(defn valor-descontado 
  "Retorna 90% do valor bruto"
  [valor-bruto]
  (* valor-bruto 0.9))

(valor-descontado 100)

; Refatorando essa função valor-descontado para algo "mais complexo"

(defn valor-descontado
  "Assim fica claro que o valor descontado é 10%."
  [valor-bruto]
  (* valor-bruto (- 1 0.10)))

(valor-descontado 100)

(defn valor-descontado-let
  "Retorna o desconto de 10% do valor bruto"
  [valor-bruto]
  (let [desconto 0.10]
    (println "Calculando o desconto de" desconto)
    (* valor-bruto (- 1 desconto))))

(valor-descontado-let 923)

(defn valor-descontado-new
  [valor-bruto]
  (let [desconto (/ 10 100)] ;Símbolos e não VARIÁVEIS
    (* valor-bruto (- 1 desconto))))

(valor-descontado 100) 

(defn valor-descontadoo
  [valor-bruto]
  (let [taxa-de-desconto (/ 10 100)
        aplicacao-do-desconto (* valor-bruto taxa-de-desconto)]
    (- valor-bruto aplicacao-do-desconto)))

(valor-descontadoo 500)


(defn valor-descontado-com-if
  [valor-bruto]
  (if (> valor-bruto 100)
    (let [taxa-de-desconto (/ 10 100)
          desconto (* valor-bruto taxa-de-desconto)]
      (- valor-bruto desconto))
    (println "O valor bruto não é maior que 100, então não se aplica o desconto. Valor bruto:" valor-bruto)))

(valor-descontado-com-if 50)

(defn maior-que-dez? [x]
  (> x 10))

(println (maior-que-dez? 5)) ; Imprime false
(println (maior-que-dez? 15)) ; Imprime true

(defn imprimir-mensagem [x]
  (when (maior-que-dez? x)
    (println "O número é maior que 10!")))

(imprimir-mensagem 5)  ; Nada é impresso
(imprimir-mensagem 15) ; Imprime "O número é maior que 10!"

; BINDING
(def x 10)

(defn imprimir-x []
  (println x))

(defn alterar-x [novo-x]
  (binding [x novo-x]
    (println "Dentro do binding:" x)
    (imprimir-x))) ; NÃO CONSEGUI USAR O BINDING, TESTAR NOVAMENTE DPS
; CONSEGUI TESTAR USANDO LET, QUE FUNCIONA PRATICAMENTE DA MESMA FORMA

(println "Fora do binding:" x)
(imprimir-x)

(println "Após o binding:" x)
(imprimir-x)
