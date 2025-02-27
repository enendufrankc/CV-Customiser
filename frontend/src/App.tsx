import React, { useState } from 'react';
import { Link, FileText, Upload, Loader2 } from 'lucide-react';
import type { ResumeData } from './types';
import axios from 'axios';

function App() {
  const [jobUrl, setJobUrl] = useState('');
  const [file, setFile] = useState<File | null>(null);
  const [loading, setLoading] = useState(false);
  const [resumeData, setResumeData] = useState<ResumeData | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      setFile(e.target.files[0]);
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!jobUrl || !file) {
      setError('Please provide both a job posting URL and your resume.');
      return;
    }

    setLoading(true);
    setError(null);

    const formData = new FormData();
    formData.append('source', file);
    formData.append('url', jobUrl);

    try {
      const response = await axios.post('http://localhost:8000/generate', formData);
      setResumeData(response.data);
    } catch (err) {
      setError('An error occurred while processing your request.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div 
      className="min-h-screen bg-[#1a202c] text-gray-100 relative"
      style={{
        backgroundImage: `
          linear-gradient(to bottom, rgba(26, 32, 44, 0.95), rgba(26, 32, 44, 0.85)),
          url('https://images.unsplash.com/photo-1497091071254-cc9b2ba7c48a?auto=format&fit=crop&q=80')
        `,
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        backgroundAttachment: 'fixed'
      }}
    >
      <div className="container mx-auto px-4 py-12">
        <h1 className="text-5xl font-bold text-center mb-3">Resume Customizer</h1>
        <p className="text-center text-gray-300 text-lg mb-12 max-w-3xl mx-auto">
          Tailor your resume to specific job descriptions, optimizing for Applicant Tracking
          Systems (ATS) and AI resume detectors.
        </p>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 max-w-7xl mx-auto">
          {/* Left Panel - Input Form */}
          <div className="bg-[#1f2937]/90 backdrop-blur-sm rounded-xl p-8 shadow-xl border border-gray-700">
            <h2 className="text-2xl font-semibold mb-2">Get Started</h2>
            <p className="text-gray-400 mb-8">
              Upload your resume and provide a job URL to generate a tailored version
            </p>

            <form onSubmit={handleSubmit} className="space-y-6">
              <div>
                <label htmlFor="jobUrl" className="block text-sm font-medium mb-2">
                  Job URL
                </label>
                <div className="relative">
                  <div className="absolute inset-y-0 left-3 flex items-center pointer-events-none">
                    <Link className="h-5 w-5 text-gray-400" />
                  </div>
                  <input
                    id="jobUrl"
                    type="url"
                    value={jobUrl}
                    onChange={(e) => setJobUrl(e.target.value)}
                    className="w-full pl-10 pr-4 py-2 bg-[#2d3748]/70 backdrop-blur-sm rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none"
                    placeholder="https://apply.workable.com/example"
                  />
                </div>
              </div>

              <div>
                <label className="block text-sm font-medium mb-2">
                  Resume (PDF)
                </label>
                <div className="border-2 border-dashed border-gray-600 rounded-lg p-8 text-center">
                  {file ? (
                    <div className="space-y-2">
                      <FileText className="h-12 w-12 mx-auto text-blue-400" />
                      <p className="text-sm text-gray-300">{file.name}</p>
                      <p className="text-xs text-gray-400">
                        {(file.size / 1024).toFixed(1)} KB
                      </p>
                      <button
                        type="button"
                        onClick={() => setFile(null)}
                        className="text-sm text-blue-400 hover:text-blue-300"
                      >
                        Change file
                      </button>
                    </div>
                  ) : (
                    <label
                      htmlFor="resume-upload"
                      className="cursor-pointer block space-y-2"
                    >
                      <Upload className="h-12 w-12 mx-auto text-gray-400" />
                      <span className="text-sm text-gray-400 block">
                        Click to upload your resume (PDF)
                      </span>
                    </label>
                  )}
                  <input
                    type="file"
                    accept=".pdf"
                    onChange={handleFileChange}
                    className="hidden"
                    id="resume-upload"
                  />
                </div>
              </div>

              <button
                type="submit"
                disabled={loading}
                className="w-full bg-blue-500 hover:bg-blue-600 py-3 px-4 rounded-lg font-medium flex items-center justify-center gap-2 disabled:opacity-50 transition-colors"
              >
                {loading ? (
                  <>
                    <Loader2 className="h-5 w-5 animate-spin" />
                    Generating...
                  </>
                ) : (
                  'Generate Resume'
                )}
              </button>

              {error && (
                <div className="p-4 bg-red-900/50 text-red-200 rounded-lg text-sm">
                  {error}
                </div>
              )}
            </form>
          </div>

          {/* Right Panel - Preview */}
          <div className="bg-[#1f2937]/90 backdrop-blur-sm rounded-xl p-8 shadow-xl border border-gray-700 flex flex-col items-center justify-center min-h-[500px]">
            {resumeData ? (
              <div className="w-full space-y-6">
                <h2 className="text-2xl font-bold">{resumeData.name}</h2>
                <p className="text-gray-400">{resumeData.title}</p>

                <div className="space-y-4">
                  <h3 className="text-lg font-semibold">Contact Information</h3>
                  <div className="grid grid-cols-2 gap-2 text-sm">
                    <p>Email: {resumeData.contact.email}</p>
                    <p>Phone: {resumeData.contact.phone}</p>
                    {resumeData.contact.github && (
                      <p>GitHub: {resumeData.contact.github}</p>
                    )}
                    {resumeData.contact.linkedin && (
                      <p>LinkedIn: {resumeData.contact.linkedin}</p>
                    )}
                  </div>
                </div>

                <div className="space-y-2">
                  <h3 className="text-lg font-semibold">Summary</h3>
                  <p className="text-gray-300 text-sm">{resumeData.summary}</p>
                </div>

                <div className="space-y-2">
                  <h3 className="text-lg font-semibold">Technical Skills</h3>
                  <div className="space-y-2">
                    {Object.entries(resumeData.technical_skills.skills).map(
                      ([category, skills]) => (
                        <div key={category}>
                          <span className="font-medium">{category}:</span>{' '}
                          <span className="text-gray-300 text-sm">
                            {skills.join(', ')}
                          </span>
                        </div>
                      )
                    )}
                  </div>
                </div>
              </div>
            ) : (
              <div className="text-center space-y-4">
                <FileText className="h-16 w-16 mx-auto text-gray-600" />
                <h3 className="text-xl font-semibold">
                  Your tailored resume will appear here
                </h3>
                <p className="text-gray-400 text-sm max-w-md">
                  Fill out the form and submit to generate a professionally tailored
                  resume optimized for applicant tracking systems
                </p>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;