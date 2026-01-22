'use client';

import { useLanguage } from '@/context/LanguageContext';
import { motion } from 'framer-motion';

export default function AboutPage() {
  const { t } = useLanguage();

  return (
    <div className="container-custom py-20 max-w-4xl">
      <motion.div 
        initial={{ opacity: 0, x: -20 }}
        animate={{ opacity: 1, x: 0 }}
      >
        <h1 className="text-4xl md:text-5xl font-bold mb-8">{t.nav.about}</h1>
        
        <div className="prose prose-lg dark:prose-invert">
          <p>
            Hello! I'm Viktor, a dedicated Software Engineer with a passion for building 
            elegant, efficient, and user-centric digital solutions. With expertise in 
            modern web technologies like React, Next.js, and Django, I bridge the gap 
            between robust back-end logic and stunning front-end interfaces.
          </p>
          <p>
            My journey in tech is driven by curiosity and a commitment to continuous 
            learning. Whether I'm architecting scalable APIs or crafting pixel-perfect 
            animations, I always prioritize performance and accessibility.
          </p>
          
          <h2 className="text-2xl font-bold mt-12 mb-4">What I Do</h2>
          <ul>
            <li><strong>Full-Stack Development:</strong> Building end-to-end applications from scratch.</li>
            <li><strong>API Design:</strong> Crafting clean, RESTful services with Django REST Framework.</li>
            <li><strong>UI/UX Engineering:</strong> Creating responsive and animated interfaces with Tailwind and Framer Motion.</li>
            <li><strong>Open Source:</strong> Contributing to the community and sharing my knowledge via blog posts and notes.</li>
          </ul>

          <h2 className="text-2xl font-bold mt-12 mb-4">My Philosophy</h2>
          <p>
            I believe that code should not only work but also be maintainable and readable. 
            Clean architecture and clear communication are the foundations of every successful 
            project.
          </p>
        </div>
      </motion.div>
    </div>
  );
}
