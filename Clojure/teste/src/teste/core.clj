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
