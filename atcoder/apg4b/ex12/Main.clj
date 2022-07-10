
(use '[clojure.string :refer [split]])


(let [input (read-line)
      [plus minus] ((juxt (fn [i] (count (filter #(= % \+) i)))
                          (fn [i] (count (filter #(= % \-) i)))) input)]
  (println (reduce + 1 (concat (repeat plus 1) (repeat minus -1)))))
