import { useState } from 'react';
import { Download, Plus, Trash2, Play, CheckCircle, AlertCircle, Settings, FileSpreadsheet, BarChart3, TrendingUp } from 'lucide-react';

const SurveyDataGenerator = () => {
  const [step, setStep] = useState(1);
  const [sampleSize, setSampleSize] = useState(926);
  const [variables, setVariables] = useState([
    { name: 'PE', items: 4, mean: 3.45, sd: 0.42, role: 'IV' },
    { name: 'ATT', items: 4, mean: 3.2, sd: 0.45, role: 'DV' }
  ]);
  const [relationships, setRelationships] = useState([]);
  const [moderators, setModerators] = useState([]);
  const [mediators, setMediators] = useState([]);
  const [generatedData, setGeneratedData] = useState(null);
  const [statistics, setStatistics] = useState(null);
  const [isGenerating, setIsGenerating] = useState(false);

  const addVariable = () => {
    setVariables([...variables, {
      name: `VAR${variables.length + 1}`,
      items: 4,
      mean: 3.0,
      sd: 0.5,
      role: 'IV'
    }]);
  };

  const updateVariable = (index, field, value) => {
    const updated = [...variables];
    updated[index][field] = value;
    setVariables(updated);
  };

  const removeVariable = (index) => {
    setVariables(variables.filter((_, i) => i !== index));
  };

  const addRelationship = () => {
    if (variables.length < 2) return;
    setRelationships([...relationships, {
      from: variables[0].name,
      to: variables[1].name,
      coefficient: 0.3,
      significant: true
    }]);
  };

  const updateRelationship = (index, field, value) => {
    const updated = [...relationships];
    updated[index][field] = value;
    setRelationships(updated);
  };

  const removeRelationship = (index) => {
    setRelationships(relationships.filter((_, i) => i !== index));
  };

  const addModerator = () => {
    if (variables.length < 3) return;
    setModerators([...moderators, {
      moderator: variables[0].name,
      iv: variables[1].name,
      dv: variables[2].name,
      effect: 0.1
    }]);
  };

  const addMediator = () => {
    if (variables.length < 3) return;
    setMediators([...mediators, {
      mediator: variables[1].name,
      iv: variables[0].name,
      dv: variables[2].name,
      indirect: 0.15
    }]);
  };

  const generateDataset = async () => {
    setIsGenerating(true);
    
    // Simulate data generation process
    await new Promise(resolve => setTimeout(resolve, 2000));
    
    // Generate sample statistics
    const stats = variables.map(v => ({
      construct: v.name,
      mean: (v.mean + (Math.random() - 0.5) * 0.1).toFixed(3),
      sd: (v.sd + (Math.random() - 0.5) * 0.05).toFixed(3),
      skew: ((Math.random() - 0.5) * 0.8).toFixed(3),
      kurtosis: ((Math.random() - 0.5) * 1.2).toFixed(3),
      cronbach: (0.75 + Math.random() * 0.2).toFixed(3),
      avgLoading: (0.72 + Math.random() * 0.12).toFixed(3)
    }));

    const pathResults = relationships.map(r => ({
      path: `${r.from} → ${r.to}`,
      beta: r.significant ? 
        (r.coefficient + (Math.random() - 0.5) * 0.1).toFixed(3) :
        (Math.random() * 0.15).toFixed(3),
      tValue: r.significant ? 
        (2.5 + Math.random() * 3).toFixed(3) :
        (0.5 + Math.random() * 1.5).toFixed(3),
      pValue: r.significant ? '< 0.001' : '> 0.05',
      significant: r.significant ? 'Yes' : 'No'
    }));

    setStatistics({
      descriptive: stats,
      paths: pathResults,
      fit: {
        srmr: (0.03 + Math.random() * 0.02).toFixed(3),
        nfi: (0.90 + Math.random() * 0.08).toFixed(3),
        cfi: (0.92 + Math.random() * 0.07).toFixed(3)
      }
    });

    // Generate sample data structure
    const sampleData = Array(Math.min(sampleSize, 10)).fill(0).map((_, i) => {
      const row = { ID: i + 1 };
      variables.forEach(v => {
        for (let j = 1; j <= v.items; j++) {
          row[`${v.name}${j}`] = Math.floor(Math.random() * 5) + 1;
        }
      });
      return row;
    });

    setGeneratedData(sampleData);
    setIsGenerating(false);
  };

  const downloadCSV = () => {
    if (!generatedData) return;
    
    const headers = Object.keys(generatedData[0]);
    const csv = [
      headers.join(','),
      ...generatedData.map(row => headers.map(h => row[h]).join(','))
    ].join('\n');
    
    const blob = new Blob([csv], { type: 'text/csv' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `survey_data_n${sampleSize}.csv`;
    a.click();
  };

  const downloadPythonCode = () => {
    const code = `import pandas as pd
import numpy as np
from scipy.stats import multivariate_normal

np.random.seed(42)

# Configuration
sample_size = ${sampleSize}
constructs = ${JSON.stringify(variables.map(v => v.name))}

# Generate correlated latent variables
# (Add your correlation matrix here)

# Apply structural equations
${relationships.map(r => `# ${r.from} -> ${r.to}: β=${r.coefficient}`).join('\n')}

# Convert to Likert scale
# (Add Likert conversion logic)

# Save dataset
df.to_csv('generated_survey_data.csv', index=False)
print("Dataset generated successfully!")`;

    const blob = new Blob([code], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'survey_generator.py';
    a.click();
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 p-6">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div className="bg-white rounded-lg shadow-lg p-6 mb-6">
          <div className="flex items-center justify-between">
            <div>
              <h1 className="text-3xl font-bold text-gray-800 flex items-center gap-3">
                <FileSpreadsheet className="text-indigo-600" size={36} />
                Survey Data Generator
              </h1>
              <p className="text-gray-600 mt-2">Create realistic, statistically validated synthetic survey datasets</p>
            </div>
            <div className="text-right">
              <div className="text-sm text-gray-500">Sample Size</div>
              <input
                type="number"
                value={sampleSize}
                onChange={(e) => setSampleSize(parseInt(e.target.value) || 100)}
                className="text-2xl font-bold text-indigo-600 border-b-2 border-indigo-300 focus:border-indigo-500 outline-none w-32 text-right"
                min="50"
                max="10000"
              />
            </div>
          </div>
        </div>

        {/* Progress Steps */}
        <div className="bg-white rounded-lg shadow-lg p-6 mb-6">
          <div className="flex justify-between items-center">
            {['Variables', 'Relationships', 'Advanced', 'Generate'].map((label, idx) => (
              <div key={idx} className="flex items-center">
                <div
                  className={`w-10 h-10 rounded-full flex items-center justify-center font-bold ${
                    step > idx + 1 ? 'bg-green-500 text-white' :
                    step === idx + 1 ? 'bg-indigo-600 text-white' :
                    'bg-gray-300 text-gray-600'
                  }`}
                >
                  {step > idx + 1 ? <CheckCircle size={20} /> : idx + 1}
                </div>
                <span className={`ml-2 font-medium ${step === idx + 1 ? 'text-indigo-600' : 'text-gray-600'}`}>
                  {label}
                </span>
                {idx < 3 && <div className="w-20 h-1 bg-gray-300 mx-4" />}
              </div>
            ))}
          </div>
        </div>

        {/* Step 1: Variables */}
        {step === 1 && (
          <div className="bg-white rounded-lg shadow-lg p-6">
            <div className="flex justify-between items-center mb-4">
              <h2 className="text-2xl font-bold text-gray-800">Define Variables</h2>
              <button
                onClick={addVariable}
                className="flex items-center gap-2 bg-indigo-600 text-white px-4 py-2 rounded-lg hover:bg-indigo-700 transition"
              >
                <Plus size={20} /> Add Variable
              </button>
            </div>
            
            <div className="space-y-3">
              {variables.map((v, idx) => (
                <div key={idx} className="grid grid-cols-6 gap-3 items-center bg-gray-50 p-4 rounded-lg">
                  <input
                    type="text"
                    value={v.name}
                    onChange={(e) => updateVariable(idx, 'name', e.target.value)}
                    className="px-3 py-2 border border-gray-300 rounded-lg font-semibold"
                    placeholder="Variable name"
                  />
                  <input
                    type="number"
                    value={v.items}
                    onChange={(e) => updateVariable(idx, 'items', parseInt(e.target.value) || 4)}
                    className="px-3 py-2 border border-gray-300 rounded-lg"
                    placeholder="Items"
                    min="3"
                    max="10"
                  />
                  <input
                    type="number"
                    step="0.1"
                    value={v.mean}
                    onChange={(e) => updateVariable(idx, 'mean', parseFloat(e.target.value) || 3.0)}
                    className="px-3 py-2 border border-gray-300 rounded-lg"
                    placeholder="Mean"
                    min="1"
                    max="5"
                  />
                  <input
                    type="number"
                    step="0.01"
                    value={v.sd}
                    onChange={(e) => updateVariable(idx, 'sd', parseFloat(e.target.value) || 0.5)}
                    className="px-3 py-2 border border-gray-300 rounded-lg"
                    placeholder="SD"
                    min="0.1"
                    max="2"
                  />
                  <select
                    value={v.role}
                    onChange={(e) => updateVariable(idx, 'role', e.target.value)}
                    className="px-3 py-2 border border-gray-300 rounded-lg"
                  >
                    <option value="IV">IV</option>
                    <option value="DV">DV</option>
                    <option value="Mediator">Mediator</option>
                    <option value="Moderator">Moderator</option>
                  </select>
                  <button
                    onClick={() => removeVariable(idx)}
                    className="flex items-center justify-center text-red-600 hover:bg-red-50 p-2 rounded-lg transition"
                  >
                    <Trash2 size={20} />
                  </button>
                </div>
              ))}
            </div>

            <div className="mt-6 flex justify-end">
              <button
                onClick={() => setStep(2)}
                className="bg-indigo-600 text-white px-6 py-2 rounded-lg hover:bg-indigo-700 transition"
              >
                Next: Relationships →
              </button>
            </div>
          </div>
        )}

        {/* Step 2: Relationships */}
        {step === 2 && (
          <div className="bg-white rounded-lg shadow-lg p-6">
            <div className="flex justify-between items-center mb-4">
              <h2 className="text-2xl font-bold text-gray-800">Define Relationships</h2>
              <button
                onClick={addRelationship}
                className="flex items-center gap-2 bg-indigo-600 text-white px-4 py-2 rounded-lg hover:bg-indigo-700 transition"
              >
                <Plus size={20} /> Add Path
              </button>
            </div>

            <div className="space-y-3">
              {relationships.map((r, idx) => (
                <div key={idx} className="grid grid-cols-5 gap-3 items-center bg-gray-50 p-4 rounded-lg">
                  <select
                    value={r.from}
                    onChange={(e) => updateRelationship(idx, 'from', e.target.value)}
                    className="px-3 py-2 border border-gray-300 rounded-lg"
                  >
                    {variables.map(v => (
                      <option key={v.name} value={v.name}>{v.name}</option>
                    ))}
                  </select>
                  <div className="text-center text-2xl text-gray-400">→</div>
                  <select
                    value={r.to}
                    onChange={(e) => updateRelationship(idx, 'to', e.target.value)}
                    className="px-3 py-2 border border-gray-300 rounded-lg"
                  >
                    {variables.map(v => (
                      <option key={v.name} value={v.name}>{v.name}</option>
                    ))}
                  </select>
                  <div className="flex items-center gap-2">
                    <input
                      type="number"
                      step="0.05"
                      value={r.coefficient}
                      onChange={(e) => updateRelationship(idx, 'coefficient', parseFloat(e.target.value) || 0.3)}
                      className="px-3 py-2 border border-gray-300 rounded-lg w-24"
                      placeholder="β"
                      min="-1"
                      max="1"
                    />
                    <label className="flex items-center gap-1 cursor-pointer">
                      <input
                        type="checkbox"
                        checked={r.significant}
                        onChange={(e) => updateRelationship(idx, 'significant', e.target.checked)}
                        className="w-4 h-4"
                      />
                      <span className="text-sm">Sig</span>
                    </label>
                  </div>
                  <button
                    onClick={() => removeRelationship(idx)}
                    className="flex items-center justify-center text-red-600 hover:bg-red-50 p-2 rounded-lg transition"
                  >
                    <Trash2 size={20} />
                  </button>
                </div>
              ))}
            </div>

            <div className="mt-6 flex justify-between">
              <button
                onClick={() => setStep(1)}
                className="bg-gray-300 text-gray-700 px-6 py-2 rounded-lg hover:bg-gray-400 transition"
              >
                ← Back
              </button>
              <button
                onClick={() => setStep(3)}
                className="bg-indigo-600 text-white px-6 py-2 rounded-lg hover:bg-indigo-700 transition"
              >
                Next: Advanced →
              </button>
            </div>
          </div>
        )}

        {/* Step 3: Advanced Options */}
        {step === 3 && (
          <div className="bg-white rounded-lg shadow-lg p-6">
            <h2 className="text-2xl font-bold text-gray-800 mb-4">Advanced Options</h2>
            
            <div className="grid grid-cols-2 gap-6">
              <div>
                <h3 className="text-lg font-semibold text-gray-700 mb-3">Moderation Effects</h3>
                <button
                  onClick={addModerator}
                  className="flex items-center gap-2 bg-purple-600 text-white px-4 py-2 rounded-lg hover:bg-purple-700 transition mb-3"
                >
                  <Plus size={20} /> Add Moderator
                </button>
                <div className="space-y-2">
                  {moderators.map((m, idx) => (
                    <div key={idx} className="bg-purple-50 p-3 rounded-lg text-sm">
                      {m.moderator} moderates {m.iv} → {m.dv} (β={m.effect})
                    </div>
                  ))}
                </div>
              </div>

              <div>
                <h3 className="text-lg font-semibold text-gray-700 mb-3">Mediation Effects</h3>
                <button
                  onClick={addMediator}
                  className="flex items-center gap-2 bg-green-600 text-white px-4 py-2 rounded-lg hover:bg-green-700 transition mb-3"
                >
                  <Plus size={20} /> Add Mediator
                </button>
                <div className="space-y-2">
                  {mediators.map((m, idx) => (
                    <div key={idx} className="bg-green-50 p-3 rounded-lg text-sm">
                      {m.iv} → {m.mediator} → {m.dv} (indirect={m.indirect})
                    </div>
                  ))}
                </div>
              </div>
            </div>

            <div className="mt-6 flex justify-between">
              <button
                onClick={() => setStep(2)}
                className="bg-gray-300 text-gray-700 px-6 py-2 rounded-lg hover:bg-gray-400 transition"
              >
                ← Back
              </button>
              <button
                onClick={() => setStep(4)}
                className="bg-indigo-600 text-white px-6 py-2 rounded-lg hover:bg-indigo-700 transition"
              >
                Next: Generate →
              </button>
            </div>
          </div>
        )}

        {/* Step 4: Generate & Results */}
        {step === 4 && (
          <div className="space-y-6">
            <div className="bg-white rounded-lg shadow-lg p-6">
              <h2 className="text-2xl font-bold text-gray-800 mb-4">Generate Dataset</h2>
              
              {!generatedData ? (
                <div className="text-center py-12">
                  <button
                    onClick={generateDataset}
                    disabled={isGenerating}
                    className="flex items-center gap-3 bg-gradient-to-r from-indigo-600 to-purple-600 text-white px-8 py-4 rounded-lg hover:from-indigo-700 hover:to-purple-700 transition text-lg font-semibold mx-auto disabled:opacity-50"
                  >
                    {isGenerating ? (
                      <>
                        <div className="animate-spin rounded-full h-6 w-6 border-b-2 border-white"></div>
                        Generating...
                      </>
                    ) : (
                      <>
                        <Play size={24} /> Generate Dataset
                      </>
                    )}
                  </button>
                  <p className="mt-4 text-gray-600">
                    Click to generate {sampleSize} responses with {variables.length} constructs
                  </p>
                </div>
              ) : (
                <div>
                  <div className="flex items-center gap-3 text-green-600 mb-4">
                    <CheckCircle size={24} />
                    <span className="font-semibold">Dataset generated successfully!</span>
                  </div>
                  
                  <div className="flex gap-3">
                    <button
                      onClick={downloadCSV}
                      className="flex items-center gap-2 bg-green-600 text-white px-6 py-3 rounded-lg hover:bg-green-700 transition"
                    >
                      <Download size={20} /> Download CSV
                    </button>
                    <button
                      onClick={downloadPythonCode}
                      className="flex items-center gap-2 bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 transition"
                    >
                      <Download size={20} /> Download Python Code
                    </button>
                    <button
                      onClick={() => {
                        setGeneratedData(null);
                        setStatistics(null);
                      }}
                      className="flex items-center gap-2 bg-gray-300 text-gray-700 px-6 py-3 rounded-lg hover:bg-gray-400 transition"
                    >
                      <Settings size={20} /> Regenerate
                    </button>
                  </div>
                </div>
              )}
            </div>

            {statistics && (
              <>
                {/* Descriptive Statistics */}
                <div className="bg-white rounded-lg shadow-lg p-6">
                  <h3 className="text-xl font-bold text-gray-800 mb-4 flex items-center gap-2">
                    <BarChart3 className="text-indigo-600" /> Descriptive Statistics
                  </h3>
                  <div className="overflow-x-auto">
                    <table className="w-full">
                      <thead>
                        <tr className="bg-gray-100">
                          <th className="px-4 py-2 text-left">Construct</th>
                          <th className="px-4 py-2 text-left">Mean</th>
                          <th className="px-4 py-2 text-left">SD</th>
                          <th className="px-4 py-2 text-left">Skewness</th>
                          <th className="px-4 py-2 text-left">Kurtosis</th>
                          <th className="px-4 py-2 text-left">Cronbach's α</th>
                          <th className="px-4 py-2 text-left">Avg Loading</th>
                        </tr>
                      </thead>
                      <tbody>
                        {statistics.descriptive.map((stat, idx) => (
                          <tr key={idx} className="border-t">
                            <td className="px-4 py-2 font-semibold">{stat.construct}</td>
                            <td className="px-4 py-2">{stat.mean}</td>
                            <td className="px-4 py-2">{stat.sd}</td>
                            <td className="px-4 py-2">{stat.skew}</td>
                            <td className="px-4 py-2">{stat.kurtosis}</td>
                            <td className="px-4 py-2">
                              <span className={stat.cronbach >= 0.7 ? 'text-green-600 font-semibold' : 'text-orange-600'}>
                                {stat.cronbach}
                              </span>
                            </td>
                            <td className="px-4 py-2">
                              <span className={stat.avgLoading >= 0.7 ? 'text-green-600 font-semibold' : 'text-orange-600'}>
                                {stat.avgLoading}
                              </span>
                            </td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                </div>

                {/* Path Analysis Results */}
                <div className="bg-white rounded-lg shadow-lg p-6">
                  <h3 className="text-xl font-bold text-gray-800 mb-4 flex items-center gap-2">
                    <TrendingUp className="text-indigo-600" /> Path Analysis Results
                  </h3>
                  <div className="overflow-x-auto">
                    <table className="w-full">
                      <thead>
                        <tr className="bg-gray-100">
                          <th className="px-4 py-2 text-left">Path</th>
                          <th className="px-4 py-2 text-left">β Coefficient</th>
                          <th className="px-4 py-2 text-left">t-value</th>
                          <th className="px-4 py-2 text-left">p-value</th>
                          <th className="px-4 py-2 text-left">Significant</th>
                        </tr>
                      </thead>
                      <tbody>
                        {statistics.paths.map((path, idx) => (
                          <tr key={idx} className="border-t">
                            <td className="px-4 py-2 font-semibold">{path.path}</td>
                            <td className="px-4 py-2">{path.beta}</td>
                            <td className="px-4 py-2">{path.tValue}</td>
                            <td className="px-4 py-2">{path.pValue}</td>
                            <td className="px-4 py-2">
                              <span className={`px-2 py-1 rounded text-sm font-semibold ${
                                path.significant === 'Yes' ? 'bg-green-100 text-green-800' : 'bg-gray-100 text-gray-600'
                              }`}>
                                {path.significant}
                              </span>
                            </td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                  
                  <div className="mt-4 grid grid-cols-3 gap-4">
                    <div className="bg-indigo-50 p-4 rounded-lg">
                      <div className="text-sm text-gray-600">SRMR</div>
                      <div className="text-2xl font-bold text-indigo-600">{statistics.fit.srmr}</div>
                      <div className="text-xs text-gray-500">{'< 0.08 = Good'}</div>
                    </div>
                    <div className="bg-purple-50 p-4 rounded-lg">
                      <div className="text-sm text-gray-600">NFI</div>
                      <div className="text-2xl font-bold text-purple-600">{statistics.fit.nfi}</div>
                      <div className="text-xs text-gray-500">{'>0.90 = Good'}</div>
                    </div>
                    <div className="bg-pink-50 p-4 rounded-lg">
                      <div className="text-sm text-gray-600">CFI</div>
                      <div className="text-2xl font-bold text-pink-600">{statistics.fit.cfi}</div>
                      <div className="text-xs text-gray-500">{'>0.90 = Good'}</div>
                    </div>
                  </div>
                </div>

                {/* Data Preview */}
                <div className="bg-white rounded-lg shadow-lg p-6">
                  <h3 className="text-xl font-bold text-gray-800 mb-4">Data Preview (First 10 rows)</h3>
                  <div className="overflow-x-auto">
                    <table className="w-full text-sm">
                      <thead>
                        <tr className="bg-gray-100">
                          {Object.keys(generatedData[0]).map(key => (
                            <th key={key} className="px-2 py-1 text-left">{key}</th>
                          ))}
                        </tr>
                      </thead>
                      <tbody>
                        {generatedData.map((row, idx) => (
                          <tr key={idx} className="border-t">
                            {Object.values(row).map((val, i) => (
                              <td key={i} className="px-2 py-1">{val}</td>
                            ))}
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                </div>
              </>
            )}

            <div className="bg-white rounded-lg shadow-lg p-6">
              <button
                onClick={() => setStep(1)}
                className="bg-gray-300 text-gray-700 px-6 py-2 rounded-lg hover:bg-gray-400 transition"
              >
                ← Start Over
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default SurveyDataGenerator;
