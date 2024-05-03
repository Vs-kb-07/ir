def calculate_metrics(ret,rel):
    tru_po = len(ret.intersection(rel))
    fal_po = len(ret.difference(rel))
    fal_neg = len(rel.difference(ret))
    print("TruePositive: ", tru_po
      ,"\nFalse Positive: ", fal_po
      ,"\nFalse Negative: ", fal_neg ,"\n")

    precision = tru_po / (tru_po + fal_po)
    recall = tru_po / (tru_po + fal_neg)
    f_measure = 2 * precision * recall / (precision + recall)
    return precision, recall, f_measure
    ret= set(["doc1", "doc2", "doc3"]) 
    rel= set(["doc1", "doc4"])
precision, recall, f_measure = calculate_metrics(ret, rel)
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F-measure: {f_measure}")
