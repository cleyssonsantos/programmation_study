(ns teste.aula4)

(def lista [1 2 3 4 5 6 7 8 9 10])

(doseq [item lista]
  (println item))

(def lista1 [30 20 100 422 542])
(println lista1)

(def nova-lista (map #(+ 3 %) lista1))

(println nova-lista)

(doseq [item nova-lista]
  (println item))

