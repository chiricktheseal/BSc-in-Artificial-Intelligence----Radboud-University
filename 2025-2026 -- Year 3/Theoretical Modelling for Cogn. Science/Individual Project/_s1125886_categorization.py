import pandas as pd
import matplotlib.pyplot as plt

objects = ['A', 'B', 'C']

similarity_matrix = {
    ('A', 'B'): 0.8,
    ('A', 'C'): 0.7,
    ('B', 'C'): 0.9,
    # Symmetric entries
    ('B', 'A'): 0.8,
    ('C', 'A'): 0.7,
    ('C', 'B'): 0.9
}

# Helper function to get similarity
def s(o1, o2):
    return similarity_matrix.get((o1, o2), 0)

# Define lambda values to test
lambda_values = [0, 0.5,  1, 2, 4,6, 8, 10]


all_partitions = [
    [['A'], ['B'], ['C']],              # 3 clusters
    [['A', 'B'], ['C']],                # 2 clusters
    [['A', 'C'], ['B']],                # 2 clusters
    [['B', 'C'], ['A']],                # 2 clusters
    [['A', 'B', 'C']]                   # 1 cluster
]

partition_names = [
    "P1: {A},{B},{C}",
    "P2: {A,B},{C}",
    "P3: {A,C},{B}",
    "P4: {B,C},{A}",
    "P5: {A,B,C}"
]

print(f"All possible partitions for objects  {objects}:")
for i, (part, name) in enumerate(zip(all_partitions, partition_names)):
    print(f"  {i+1}. {name}")
print()



def within_raw(partition):
    """Raw within-cluster similarity (sum)"""
    total = 0
    for cluster in partition:
        for i in range(len(cluster)):
            for j in range(i+1, len(cluster)):
                total += s(cluster[i], cluster[j])
    return total

def between_raw(partition):
    """Raw between-cluster similarity (sum)"""
    total = 0
    for i in range(len(partition)):
        for j in range(i+1, len(partition)):
            for obj1 in partition[i]:
                for obj2 in partition[j]:
                    total += s(obj1, obj2)
    return total

def normalized_within(partition):
    """
    Normalized within-cluster similarity:
    Average similarity of pairs within categories
    """
    W_raw = within_raw(partition)
    
    # Count number of pairs within categories
    total_pairs_within = 0
    for cluster in partition:
        n = len(cluster)
        total_pairs_within += n * (n - 1) / 2
    
    # If no pairs (all singletons), return 0
    if total_pairs_within == 0:
        return 0
    return W_raw / total_pairs_within

def normalized_between(partition):
    """
    Normalized between-category similarity:
    Average similarity of pairs between categories
    """
    B_raw = between_raw(partition)
    
    # Count number of pairs between categories
    total_pairs_between = 0
    for i in range(len(partition)):
        for j in range(i+1, len(partition)):
            total_pairs_between += len(partition[i]) * len(partition[j])
    
    # If no pairs (only 1 category), return 0
    if total_pairs_between == 0:
        return 0
    return B_raw / total_pairs_between

def objective_function(partition, lambda_val):
    """
    Objective function F(C) = Within(C) - λ * Between(C)
    """
    W = normalized_within(partition)
    B = normalized_between(partition)
    
    return W - lambda_val * B

def get_partition_info(partition):
    """Get information about partition"""
    W = normalized_within(partition)
    B = normalized_between(partition)
    W_raw = within_raw(partition)
    B_raw = between_raw(partition)
    
    
    # Count pairs for normalization
    pairs_within = sum(len(c)*(len(c)-1)//2 for c in partition)
    pairs_between = 0
    for i in range(len(partition)):
        for j in range(i+1, len(partition)):
            pairs_between += len(partition[i]) * len(partition[j])
    
    return {
        'W': W,
        'B': B,
        'W_raw': W_raw,
        'B_raw': B_raw,
        'pairs_within': pairs_within,
        'pairs_between': pairs_between,
        'num_clusters': len(partition)
    }



all_results_normalized = []

for lambda_val in lambda_values:
    print(f"\n{'='*80}")
    print(f"TABLE FOR λ  = {lambda_val}")
    print(f"\n{'='*80}")
    print("\nPartition           | Within_norm | Between_norm | F_norm(C) | Categories")
    print("-" * 70)
    
    partition_results = []
    
    for part_name, partition in zip(partition_names, all_partitions):
        info = get_partition_info(partition)
        
        W_norm = info['W']
        B_norm = info['B']
        F_norm = W_norm - lambda_val * B_norm
        
        # Shorten name for table
        short_name = part_name.split(": ")[1] if ": " in part_name else part_name
        
        # Print table row
        print(f"{short_name:<18} | {W_norm:>10.3f}  | {B_norm:>12.3f} | {F_norm:>9.3f} | {info['num_clusters']:>9}")
        
        # Save results
        partition_results.append({
            'partition_name': part_name,
            'partition': partition,
            'W_norm': W_norm,
            'B_norm': B_norm,
            'F_norm': F_norm,
            'num_clusters': info['num_clusters']
        })
    
    # Find best partition for this λ
    best_partition = max(partition_results, key=lambda x: x['F_norm'])
    
    print("-" * 70)
    print(f"Optimal partition for λ = {lambda_val}:")
    short_best = best_partition['partition_name'].split(": ")[1] if ": " in best_partition['partition_name'] else best_partition['partition_name']
    print(f"  {short_best}")
    print(f"  F_norm(C) = {best_partition['F_norm']:.3f}")
    print(f"  Within_norm = {best_partition['W_norm']:.3f}, Between_norm = {best_partition['B_norm']:.3f}")
    print(f"  Category number: {best_partition['num_clusters']}")
    
    # Save for summary table
    all_results_normalized.append({
        'lambda': lambda_val,
        **best_partition
    })
    



print("\n" + "="*100)
print("SUMMARY TABLE: OPTIMAL PARTITIONS")
print("="*100)

# Create DataFrame with optimal results
optimal_df = pd.DataFrame(all_results_normalized)

print("\n" + "-"*85)
print(f"{'λ':<6} | {'Optimal Partition':<20} | {'Categories':<10} | {'Within_norm':<12} | {'Between_norm':<12} | {'F_norm(C)':<12}")
print("-"*85)

for _, row in optimal_df.iterrows():
    short_name = row['partition_name'].split(": ")[1] if ": " in row['partition_name'] else row['partition_name']
    
    print(f"{row['lambda']:<6} | {short_name:<20} | {row['num_clusters']:<10} | "
          f"{row['W_norm']:<12.3f} | {row['B_norm']:<12.3f} | {row['F_norm']:<12.3f}")

print("-"*85)


plt.figure(figsize=(10, 5))

#  N categories  vs  λ 
plt.subplot(1, 2, 1)
plt.plot(optimal_df['lambda'], optimal_df['num_clusters'], 'bo-', linewidth=3, markersize=10)
plt.xlabel('λ (lambda)', fontsize=12)
plt.ylabel('Number of categories N', fontsize=12)
plt.title('N categories  vs  λ', fontsize=14)
plt.grid(True, alpha=0.3)

for _, row in optimal_df.iterrows():
    plt.annotate(f"{int(row['num_clusters'])}", 
                (row['lambda'], row['num_clusters']),
                textcoords="offset points",
                xytext=(0,10),
                ha='center',
                fontsize=11,
                fontweight='bold')

# W_norm, B_norm  vs  λ
plt.subplot(1, 2, 2)
plt.plot(optimal_df['lambda'], optimal_df['W_norm'], 'g^-', label='W_norm(C)', linewidth=2, markersize=8)
plt.plot(optimal_df['lambda'], optimal_df['B_norm'], 'rs--', label='B_norm(C)', linewidth=2, markersize=8)
plt.xlabel('λ (lambda)', fontsize=12)
plt.ylabel('Metric values', fontsize=12)
plt.title('B_norm(C), W_norm(C)  vs  λ', fontsize=14)
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('normalized_analysis.png', dpi=300, bbox_inches='tight')
plt.show()

