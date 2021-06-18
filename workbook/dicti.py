textbook = ['According', 'to', 'consensus', 'in', 'modern', 'genetics', 'anatomically', 'modern', 'humans', 'first', 'arrived', 'on', 'the', 'Indian', 'subcontinent', 'from', 'Africa', 'between', '73,000', 'and', '55,000', 'years', 'ago.', 'However,', 'the', 'earliest', 'known', 'human', 'remains', 'in', 'South', 'Asia', 'date', 'to', '30,000', 'years', 'ago.', 'Settled', 'life,', 'which', 'involves', 'the', 'transition', 'from', 'foraging', 'to', 'farming', 'and', 'pastoralism,', 'began', 'in', 'South', 'Asia', 'around', '7,000', 'BCE.', 'At', 'the', 'site', 'of', 'Mehrgarh,', 'Balochistan,', 'Pakistan,', 'presence', 'can', 'be', 'documented', 'of', 'the', 'domestication', 'of', 'wheat', 'and', 'barley,', 'rapidly', 'followed', 'by', 'that', 'of', 'goats,', 'sheep,', 'and', 'cattle.', 'By', '4,500', 'BCE,', 'settled', 'life', 'had', 'spread', 'more', 'widely,', '', 'and', 'began', 'to', 'gradually', 'evolve', 'into', 'the', 'Indus', 'Valley', 'Civilization,', 'an', 'early', 'civilization', 'of', 'the', 'Old', 'world,', 'which', 'was', 'contemporaneous', 'with', 'Ancient', 'Egypt', 'and', 'Mesopotamia.', 'This', 'civilisation', 'flourished', 'between', '2,500', 'BCE', 'and', '1900', 'BCE', 'in', 'what', 'today', 'is', 'Pakistan', 'and', 'north-western', 'India,', 'and', 'was', 'noted', 'for', 'its', 'urban', 'planning,', 'baked', 'brick', 'houses,', 'elaborate', 'drainage,', 'and', 'water', 'supply.', 'In', 'the', 'early', 'second', 'millennium', 'BCE', 'persistent', 'drought', 'caused', 'the', 'population', 'of', 'the', 'Indus', 'Valley', 'to', 'scatter', 'from', 'large', 'urban', 'centres', 'to', 'villages.', 'Around', 'the', 'same', 'time,', 'Indo-Aryan', 'tribes', 'moved', 'into', 'the', 'Punjab', 'from', 'Central', 'Asia', 'in', 'several', 'waves', 'of', 'migration.', 'Their', 'Vedic', 'period', '(1500-500', 'BCE)', 'was', 'marked', 'by', 'the', 'composition', 'of', 'the', 'Vedas,', 'large', 'collections', 'of', 'hymns', 'of', 'these', 'tribes.', 'Their', 'varna', 'system,', 'which', 'evolved', 'into', 'the', 'caste', 'system,', 'consisted', 'of', 'a', 'hierarchy', 'of', 'priests,', 'warriors,', 'and', 'free', 'peasants,', 'excluded', 'indigenous', 'peoples', 'by', 'labeling', 'their', 'occupations', 'impure.', 'The', 'pastoral', 'and', 'nomadic', 'Indo-Aryans', 'spread', 'from', 'the', 'Punjab', 'into', 'the', 'Gangetic', 'plain,', 'large', 'swaths', 'of', 'which', 'they', 'deforested', 'for', 'agriculture', 'usage.', 'The', 'composition', 'of', 'Vedic', 'texts', 'ended', 'around', '600', 'BCE,', 'when', 'a', 'new,', 'interregional', 'culture', 'arose.', 'Small', 'chieftaincies,', 'or', 'janapadas,', 'were', 'consolidated', 'into', 'larger', 'states,', 'or', 'mahajanapadas,', 'and', 'a', 'second', 'urbanisation', 'took', 'place.', 'This', 'urbanisation', 'was', 'accompanied', 'by', 'the', 'rise', 'of', 'new', 'ascetic', 'movements', 'in', 'Greater', 'Magadha,', 'including', 'Jainism', 'and', 'Buddhism,', 'which', 'opposed', 'the', 'growing', 'influence', 'of', 'Brahmanism', 'and', 'the', 'primacy', 'of', 'rituals,', 'presided', 'by', 'Brahmin', 'priests,', 'that', 'had', 'come', 'to', 'be', 'associated', 'with', 'Vedic', 'religion,', 'and', 'gave', 'rise', 'to', 'new', 'religious', 'concepts.[5]', 'In', 'response', 'to', 'the', 'success', 'of', 'these', 'movements,', 'Vedic', 'Brahmanism', 'was', 'synthesised', 'with', 'the', 'preexisting', 'religious', 'cultures', 'of', 'the', 'subcontinent,', 'giving', 'rise', 'to', 'Hinduism.']


def word_count(textbook):
    new_text = {}
    for word in textbook:
        if word in new_text:
            new_text[word] += 1
        else:
            new_text[word] = 1

    return new_text

print(word_count((textbook)))

# def common_words(freqs):
#     values = freqs.values()
#     best = max(values)
#     words = []
#     for i in freqs:
#         if freqs[i] == best:
#             words.append(i)
#     return (words, best)
#
# def words_often(freqs, min_time):
#     result = []
#     done = False
#     while not done:
#         temp = common_words(freqs)
#         if temp[1] >= min_time:
#             result.append(temp)
#             for w in temp[0]:
#                 del(freqs[w])
#         else:
#             done = True
#     return result
# print(words_often(india, 5))
