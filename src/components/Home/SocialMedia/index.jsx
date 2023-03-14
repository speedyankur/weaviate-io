import React, { useEffect, useState } from 'react';

import styles from './styles.module.scss';
import { tweetsArray } from './tweets';
import TweetEmbed from 'react-tweet-embed';
import { useColorMode } from '@docusaurus/theme-common';


export default function HomeSocialMedia() {
  const { colorMode } = useColorMode();

  return (
    <div className="container">
      <div className={styles.content}>
        <h2>
        Loved by Developers
        </h2>
        <p>
        Join 2,500+ Devs Building with Weaviate on Discord →
        </p>
        <div className={styles.tweetContainer}>
          {tweetsArray.map((item, index) => {
            if(index > 5) return
            return (
              <div className={styles.tweetStyle}>
                <TweetEmbed tweetId={item}  options={{theme: colorMode, conversation: 'none' }} />
              </div>
            )
          })}
          </div>
      </div>
    </div>
  );
}
