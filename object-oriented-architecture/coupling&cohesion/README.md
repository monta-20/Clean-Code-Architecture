# Cohesion & Coupling Explained with Code Examples

---

## 1. Cohesion (High Cohesion = Good)

**Definition:** How closely related the responsibilities of a module/class are.  
**Goal:** Each module should do one specific thing well.

### Types of Cohesion

| Type             | Description                                 | Example                                   |
|------------------|---------------------------------------------|-------------------------------------------|
| Functional (Best) | All parts work together for single task     | `MathCalculator` (only does math ops)     |
| Sequential       | Output of one part is input to next         | `DataProcessor` (read → process → save)   |
| Communicational  | Parts work on same data                     | `UserReport` (all methods use user data)  |
| Temporal         | Parts execute at same time                  | `AppInitializer` (setup logs, DB, config) |
| Logical          | Parts are related logically                 | `FileUtils` (unrelated file operations)   |
| Coincidental (Worst) | No meaningful relationship             | `Utils` (random helper methods)           |

---

## 2. Coupling (Loose Coupling = Good)

**Definition:** How much one module depends on another.  
**Goal:** Minimize dependencies between modules.

### Types of Coupling

| Type                | Description                          | Example                                   |
|---------------------|--------------------------------------|-------------------------------------------|
| No Coupling         | Independent modules                  | Standalone utilities                      |
| Data Coupling (Best)| Communicates via parameters          | `process(data)`                           |
| Stamp Coupling      | Passes whole data structure          | `process(employee)`                       |
| Control Coupling    | One controls flow of another         | `process(flag=True)`                      |
| External Coupling   | Depends on external systems          | Database/API calls                        |
| Common Coupling     | Shares global data                   | Global variables                          |
| Content Coupling (Worst)| Modifies internals directly      | `obj._private_data = x`                   |

---

## Visualization

### High Cohesion + Loose Coupling (Ideal)

